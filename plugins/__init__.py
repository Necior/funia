import abc
from typing import Optional

from post import Post


class Plugin:
    @property
    @abc.abstractmethod
    def enabled_channels(self):
        raise NotImplemented

    @abc.abstractmethod
    def handle_msg(self, post: Post) -> Optional[str]:
        raise NotImplemented

    def _handle_msg(self, post: Post) -> Optional[str]:
        if post.channel_name not in self.enabled_channels:
            return
        return self.handle_msg(post)
