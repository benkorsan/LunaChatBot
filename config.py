
from pyrogram import Client
from os import getenv
from dotenv import load_dotenv

HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]
    BOT_ID= environ["BOT_ID"] 
# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    BOT_ID="" 
    bot_token = ""
    ARQ_API_KEY = "Get this from @ARQRobot"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "en"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
load_dotenv()
API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID"))
TOKEN = getenv("TOKEN")
OWNERID = int(getenv("OWNERID"))  # your userid
BOT_ID = int(getenv("BOT_ID"))
DB_URL = getenv("DB_URL")
DB_NAME = getenv("DB_NAME")

