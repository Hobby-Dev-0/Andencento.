import os
from Config import Config
ENV = bool(os.environ.get("ENV", False))

if ENV:
    pass
else:
    if os.path.exists("config.py"):
        pass
Config = Config
