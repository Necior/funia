import shelve
import random
from typing import Optional

from config import ENABLED_CHANNELS
from plugins import Plugin
from post import Post


class Fortunki(Plugin):
    enabled_channels = ENABLED_CHANNELS

    def __init__(self, db_path: str):
        self.seen = set()
        self.db_path = db_path  # TODO: make it a Path

    def _get_fortunka(self) -> Optional[str]:
        with shelve.open(self.db_path) as db:
            fortunki = db["fortunki"]
        new = fortunki - self.seen
        if len(new) == 0:
            new = fortunki
            self.seen = set()
        if len(new) == 0:
            # it means there are no fortunki
            return
        fortunka = random.choice(list(new))
        self.seen.add(fortunka)
        return fortunka

    def handle_msg(self, post: Post) -> Optional[str]:
        if not post.text.startswith("!fortunka"):
            return
        if post.text == "!fortunka":
            return self._get_fortunka()
        if post.text.startswith("!fortunka dodaj "):
            fortunka = post.text.split("!fortunka dodaj ", 1)[1]
            if not fortunka:
                return "Pusta fortunka? Nie chcę."

            with shelve.open(self.db_path) as db:
                fortunki = db["fortunki"]
                fortunki.add(fortunka)
                db["fortunki"] = fortunki
            return "No spoko. Fortunka #{} dodana :)".format(len(fortunki))
