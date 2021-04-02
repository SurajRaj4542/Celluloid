if __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)

import os

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    OWNER_ID = (
        os.getenv('OWNER_ID')  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = os.getenv('OWNER_USERNAME')
    TELETHON_HASH =  os.getenv('TELETHON_HASH')
    TELETHON_ID = os.getenv('TELETHON_ID')

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')  # needed for any database modules
    REDIS_URI = os.getenv('REDIS_URI')
    MESSAGE_DUMP = os.getenv('MESSAGE_DUMP')  # needed to make sure 'save from' messages persist
    GBAN_DUMP = os.getenv('GBAN_DUMP')
    ERROR_DUMP = os.getenv('ERROR_DUMP')
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
        [1100420431, 1313665327, 1099898513, 1222035687, 1437916686, 1552092495, 1620199093, 1201425400, 1542443750, 696086626]
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        [163494588, 836190821, 446243273]
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        [1364843887, 1411671709]
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = ('/', '!')   # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = os.getenv('API_OPENWEATHER')  # OpenWeather API
    SPAMWATCH_API = os.getenv('SPAMWATCH_API') # Your SpamWatch token
    
    
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
