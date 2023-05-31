from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 BUAT 𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🔥", callback_data="telethon")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="KEMBALI", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("OWNER", url="https://t.me/MSDZULQRNN"),
         InlineKeyboardButton("BOT LAIN NYA🔎", url="https://t.me/MSPR0JECT")],
    ]

    START = """
**BUAT BOT MU SEKARANG💃**
    """

    HELP = """
✨ **Perintah Yang Tersedia

 × /start - Mulai Bot
 × /about - Tentang Bot ini
 × /ping - Untuk Mengecek Ping Bot
 × /id - Untuk Mendapatkan User ID
 × /generate - Mulai Pengambilan String
 × /cancel - Membatalkan Proses Pengambilan String
 × /restart - Merestart Proses Pengambilan String**
"""

    ABOUT = """
** Tentang Bot ini:

{} di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Simple dan Mudah!

 • Pemilik: [🄼🅂 𝗗🆉𝗨𝗟𝚀𝐔𝐑𝐍Λ𝐈𝐍](https://t.me/MSDZULQURNAIN)
 • Channel: [🄼🅂 ק𝙍♢JΞC†](https://t.me/MSPR0JECT)
 • Framework: Pyrogram
 • Language: Python

👨‍💻 Develoved by @MSDZULQURNAIN**
    """
