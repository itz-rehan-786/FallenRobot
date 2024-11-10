class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27744639
    API_HASH = "a5e9da62bcd7cc761de2490c52c89ccf"

    CASH_API_KEY = "BUATLRCHB18ICFC0"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://oaykvtmj:bsIGPV7wmId1x1CNH9eqxQVX5t25cHI3@manny.db.elephantsql.com/oaykvtmj"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002356967761)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://waifuuu0786:sungjinwoo@cluster0.uctgneu.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://i.ibb.co/KDHzCVd/photo-2024-11-10-20-08-07.jpg"

    SUPPORT_CHAT = "land_of_hunters"  of Your Telegram support group chat username where your users will go and bother you

    TOKEN = "8167388254:AAE5Fbts2L8erz7Sa_t4pqFqziQi9g06DXc"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "3LPPBQ5DET7O"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7775259302  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
