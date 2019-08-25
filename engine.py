import asyncio
import json
from typing import List

import mattermostdriver as mt

from config import PREFIX
from plugins import Plugin
from post import Post
from user import User


class Engine:
    def __init__(self, driver: mt.Driver, plugins: List[Plugin]):
        self.driver = driver
        self.plugins = plugins

    def run(self):
        self.driver.login()
        self.driver.init_websocket(self.handler)

    @asyncio.coroutine
    def handler(self, raw_message):
        msg = json.loads(raw_message)
        if not msg.get("event"):
            return
        if not msg["event"] == "posted":
            return
        self.handle_post(msg["data"])

    def handle_post(self, data):
        raw_post = json.loads(data["post"])
        post = Post(
            data["channel_name"], User(data["sender_name"]), raw_post["message"]
        )
        if post.text.startswith(PREFIX):
            return  # ignore bot's own messages to avoid infinite loop
        for plugin in self.plugins:
            response = plugin._handle_msg(post)
            if response:
                self.driver.posts.create_post(
                    options={
                        "channel_id": raw_post["channel_id"],
                        "message": PREFIX + response,
                    }
                )
