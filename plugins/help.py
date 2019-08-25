from typing import Optional

from config import ENABLED_CHANNELS
from plugins import Plugin
from post import Post


class Help(Plugin):
    enabled_channels = ENABLED_CHANNELS

    def handle_msg(self, post: Post) -> Optional[str]:
        if post.text not in {"!help", "!pomoc"}:
            return

        return (
            "Dostępne polecenia: "
            "`!pomoc`, "
            "`!fortunka`, "
            "`!fortunka dodaj [treść]`, "
            "`!321`, "
            "`!ping`, "
            "`!ficzer dodaj [treść]`."
            " (Widzisz buga? Napisz do @adrian.sadlocha.)"
        )
