from config import Config
from config import Config as Var

from .. import *

ALIVE_NAME = os.environ.get("YOUR_NAME", None)
YOUR_NAME = os.environ.get("YOUR_NAME", None)
from Config import Config

versionop = "0.0.2"
W2Hversion = versionop
botversion = versionop
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if Var.ANDENCENTO_SESSION:
    session_name = str(Var.ANDENCENTO_SESSION)
    Andencento = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    Andencento = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
