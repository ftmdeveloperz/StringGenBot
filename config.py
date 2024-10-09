from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "28776072"))
API_HASH = getenv("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")

BOT_TOKEN = getenv("BOT_TOKEN", "7515672383:AAECb1fd9IfvA32Wr44h_V7AP3JTv889LIo")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ftmserver:ftm@cluster0.fneio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(getenv("OWNER_ID", "7711039923"))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ftmbotzsuppotz")
