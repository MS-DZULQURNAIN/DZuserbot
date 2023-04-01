import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")

if not API_ID:
    raise SystemExit("API_ID Tidak tersedia. Keluar...")
elif not API_HASH:
    raise SystemExit("API_HASH Tidak tersedia. Keluar...")
elif not BOT_TOKEN:
    raise SystemExit("BOT_TOKEN Tidak tersedia. Keluar...")
'''
if not DATABASE_URL:
    print("DATABASE_URL Tidak tersedia. Keluar...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID Tidak cocok. Keluar...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
