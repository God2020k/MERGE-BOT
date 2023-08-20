import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "d14e54b0791ca1f8b0f26786439e336e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6522568638:AAH8WVUyxAXIhhKYhDPsDb9HXpSOTfgQFSU")
    TELEGRAM_API = 17627887
    OWNER = os.environ.get("OWNER", "5179682108")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Professor22k")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://King:King@file.fuxewu1.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
