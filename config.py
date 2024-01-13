import os
import time

class Config(object):

    TELEGRAM_BOT_TOKEN    = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    API_KEY  = os.environ.get("API_KEY", " nNVB1ecq09EhrAujk99r ")




    BOT_START_TIME = time.time()

