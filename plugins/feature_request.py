import random
import shelve
from typing import Optional

from config import ENABLED_CHANNELS
from plugins import Plugin
from post import Post


class FeatureRequest(Plugin):
    enabled_channels = ENABLED_CHANNELS

    def __init__(self, db_path: str):
        self.db_path = db_path  # TODO: make it a Path

    def handle_msg(self, post: Post) -> Optional[str]:
        if not post.text.startswith("!ficzer dodaj "):
            return

        feature = post.text.split("!ficzer dodaj ", 1)[1]
        if not feature:
            return "Pusty ficzer? Nie chcę."
        with shelve.open(self.db_path) as db:
            requests = db.get("requests", set())  # type: set
            requests.add(feature)
            db["requests"] = requests
        return random.choice(
            [
                "No dobra, dodałem ten ficzer do listy. Ale nic nie obiecuję!",
                "Mniam, kolejny ficzer.",
                "Źle sprecywowane zadanie, zamykam",
                "Roszczeniowi millenialsi. Ficzery to chcą, a pisać nie ma komu!",
                "Oho! To nie wiadomo będzie, czy to ficzer, czy to bug.",
                "O, ten jest spoko. Przekażę twórcy.",
                "Nie lepiej w Fifę pograć zamiast takie feature'y wymyślać?",
                "`AttributeError: 'ficzers' object has no attribute 'dodaj'` ;-)",
                "O! " + self._get_first_name(post) + " ma wreszcie jakiś pomysł!",
                "Lubię to. Dodane do listy.",
                "Dziękuję Ci za podzielenie się tym pomysłem.",
                "Lepsze ficzery od Różowej Pantery.",
                "Jakie życie taki rap; jaki ficzer taki bug.",
                "!fortunka",
                "Heh, a hxkjcjska fgnhjrtvnlgiuhfg chciał kiedyś flirtunkę.",
                "xD\n\nNo okay.",
                "Dodaję do listy, ale obiecaj, że nie będziesz pisać z "
                "Pawłem Ęckim o pierdołach związanych z Pythonem.",
                "Typowy pomysł jak na :" + self._get_first_name(post).lower() + ":",
            ]
        )

    def _get_first_name(self, post: Post) -> str:
        return post.user.user_name.split(".")[0].replace("@", "").capitalize()
