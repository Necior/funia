# funia

My simple Mattermost bot.
**Consider this piece of software unsafe**.
I've made this with specific assumptions (about users, network, security etc.) which might be not fulfilled in your case.

## How to use

1. Use Python 3.7, possibly in a virtual environment.
2. Figure out requirements and install them.
3. `cp config.py.sample config.py` and edit the latter as needed.
4. run `python funia.py`.

## TODOs / ideas / feature requests

* Automagiaclly reconnect on network failure.
* Remove unused parts of a `Token` class.

---

Made with [Python](https://www.python.org/).
Formatted with [Black](https://github.com/psf/black).
