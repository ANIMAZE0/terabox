import os
import time

class Config(object):

    TELEGRAM_BOT_TOKEN    = os.environ.get("TELEGRAM_BOT_TOKEN", "6851266521:AAHY5uq7jUQQPHSR5ad-vMoykyFVSeDR4sg")
    API_KEY  = os.environ.get("API_KEY", "nNVB1ecq09EhrAujk99r")
    GET_API_KEY  = os.environ.get("GET_API_KEY", "https://anbusec.xyz")



    BOT_START_TIME = time.time()

