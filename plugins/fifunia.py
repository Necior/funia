from typing import List, Optional

from config import FIFUNIA_CHANNELS
from plugins import Plugin
from post import Post
from user import User

HELP_MSG = "Dostępne polecenia: `!dodaj`, `!usuń`, `!status`, `!myk`."


class Fifunia(Plugin):
    enabled_channels = FIFUNIA_CHANNELS

    def __init__(self):
        self._team = list()  # type: List[User]
        self._template_inprogress = "Bieżący skład: `{} | {} | {} | {}`. " + HELP_MSG
        self._template_full = (
            "Ekipa została zebrana. "
            "Zapraszam do chill roomu. "
            "Wołam: @{}, @{}, @{} oraz @{}."
            ""
        )
        self.max_team_size = 4

    def _add_player(self, user: User) -> bool:
        if user.user_name in [u.user_name for u in self._team]:
            return False
        self._team.append(user)
        return True

    def _remove_player(self, user: User) -> bool:
        if user.user_name not in [u.user_name for u in self._team]:
            return False
        self._team = [u for u in self._team if u.user_name != user.user_name]
        return True

    @property
    def _full(self) -> bool:
        return len(self._team) == self.max_team_size

    def _clear(self):
        self._team = list()

    def _roster_msg(self):
        if self._full:
            return self._template_full.format(
                self._team[0].user_name,
                self._team[1].user_name,
                self._team[2].user_name,
                self._team[3].user_name,
            )
        else:
            names = [u.user_name for u in self._team]
            rest = ["x" for _ in range(self.max_team_size - len(self._team))]
            return self._template_inprogress.format(*(names + rest))

    def _myk(self):
        if len(self._team) == 0:
            return "Ale kto ma grać?"
        r = "Ekipa została zebrana. " "Zapraszam do chill roomu. " "Wołam: " ""
        r += ", ".join("@{}".format(u.user_name) for u in self._team[:-1])
        if len(self._team) > 1:
            r += " oraz @{}".format(self._team[-1].user_name)
        else:
            r += "@{}".format(self._team[-1].user_name)
        return r + "."

    def handle_msg(self, post: Post) -> Optional[str]:
        if post.text not in {
            "!dodaj",
            "!usun",
            "!usuń",
            "!status",
            "!dodajkurwa",
            "!myk",
            "!pomoc",
            "!help",
        }:
            return
        if post.text in {"!dodaj", "!dodajkurwa"}:
            added = self._add_player(post.user)
            if not added:
                return "Toć już jesteś na liście."
            msg = self._roster_msg()
            if self._full:
                self._clear()
            return msg
        elif post.text in {"!usun", "!usuń"}:
            removed = self._remove_player(post.user)
            if not removed:
                return "Toć nie jesteś na liście."
            return self._roster_msg()
        elif post.text in {"!status"}:
            return self._roster_msg()
        elif post.text in {"!myk"}:
            r = self._myk()
            self._clear()
            return r
        elif post.text in {"!pomoc", "!help"}:
            return HELP_MSG
