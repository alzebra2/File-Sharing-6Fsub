# (©)Codexbotz
# Recife By @lucarlossx

import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6071218707:AAHn3xGmhDff3teUI9PlzcIPhAmF8D7TSS4")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26693108"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "ab04cfbc8cc8375ac74246b89c9cb24f")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001981189291"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5572478671"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@gege")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://lqqpujrb:6LEiOr01DsTh8L7Zat1Rwe9MNkFiwsgk@tyke.db.elephantsql.com/lqqpujrb")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "L9BTX")
GROUP = os.environ.get("GROUP", "L9BTX")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001760574668"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001638712428"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001750750235"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "0"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001606025151"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001602197795"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1001988188975"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1768030466)
ADMINS.append(2010825200)
ADMINS.append(1926379604)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
