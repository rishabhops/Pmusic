import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27949531 #int(getenv("API_ID"))
API_HASH = "3dedc190864d26f174ff306ec47a83ad" #getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = "6144915111:AAFCmh-tENiyfO_lIzazlAOUpUvtK47ralQ" #getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "Hackerpushkar")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "MisQueen_Music_Bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "queen MUSIC")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "Saniya_Gz2")
EVALOP = list(map(int, getenv("EVALOP", "6195725562").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://satreopalsen:pushkar@cluster0.vlkdddb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" #getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10000"))

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001907436368"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6367495275"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = "pushakrmusjv" #getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = "HRKU-943f8dae-f1f3-429c-870d-1abd500e77fc" #getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/Pmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = "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"# your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Official_InstaPLUS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Dream99_VIP_Hub")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400000")
)  # Remember to give value in Seconds


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "250"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 ="BQF-hwMAdzQfXhx9CSatqkyr5P6H6A4cNDWFlGMW854w4gqIKoavnRyTDEHK74A8gUBe8fe9JpKm2a-nSKt3Ftw8iO_udY0Nix4PVFl82zf3CR7K3X0cOb5zaishrm32SNc77YVtVeYdC2DrtPpcev81dUVdQUGCx8TbWBr0k9nf68eI4O3DRmRtv55L8WrH29WLr00GDR5sohLZxrFRdyvUs3jySqUwJOLCJIG7l7d1qRWn7SB9846OBH88Z9Qm5GdBhzhPvGb1_dE20Hj3ZgmAk52mh8pUH-V9oAQiHWNT-SKqC8VL3MFKCaCYLdgNIAH2KPsNQ98qRS89NIS8cMMVIscsOwAAAAGoffsoAA" #getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/3acab06e04581d08a24da.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/3acab06e04581d08a24da.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7795e58425337d0455e95.jpg"
STATS_IMG_URL = "https://graph.org/file/3acab06e04581d08a24da.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
