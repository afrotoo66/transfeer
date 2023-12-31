import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 25336226))

    API_HASH = os.environ.get("API_HASH", "fc6670f0d2070c0a6defb9c25b92c384")
