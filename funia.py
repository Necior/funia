import mattermostdriver as mt

import config
from engine import Engine
from plugins.feature_request import FeatureRequest
from plugins.fifunia import Fifunia
from plugins.fortunki import Fortunki
from plugins.help import Help
from plugins.simple_responses import SimpleResponses


def main():
    def disable_https_warnings():
        import urllib3

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    disable_https_warnings()
    driver = mt.Driver(
        {
            "url": config.MATTERMOST_DOMAIN,
            "port": 443,
            "token": config.Token.access_token,
            "verify": False,
        }
    )
    plugins = [
        Fifunia(),
        Fortunki(config.DB_PATH),
        Help(),
        SimpleResponses(),
        FeatureRequest(config.DB_PATH),
    ]
    engine = Engine(driver, plugins)
    engine.run()


if __name__ == "__main__":
    main()
