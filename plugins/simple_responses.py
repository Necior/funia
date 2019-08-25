from typing import Optional

from config import ENABLED_CHANNELS
from plugins import Plugin
from post import Post


class SimpleResponses(Plugin):
    enabled_channels = ENABLED_CHANNELS

    def __init__(self):
        self.command2response = {
            "!321": "At a MINIMUM follow the 3-2-1 Rule Daily – "
            "Three hours of sleep, Two Meals, One Shower.",
            "!ping": "pong",
        }

    def handle_msg(self, post: Post) -> Optional[str]:
        return self.command2response.get(post.text)
