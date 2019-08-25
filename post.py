from user import User


class Post:
    def __init__(self, channel_name: str, user: User, text: str):
        self.channel_name = channel_name  # e.g. "test"; it's a part of URL
        self.user = user
        self.text = text
