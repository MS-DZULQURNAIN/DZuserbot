from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 MULAI MENGAMBIL STRING 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="KEMBALI", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("BANTUAN", callback_data="help"),
            InlineKeyboardButton("TENTANG SAYA", callback_data="about")
        ],
        [InlineKeyboardButton("BOT LAIN NYA🔎", url="https://t.me/MSPR0JECT")],
    ]

    START = """
**Halo {}
━━━━━━━━━━━━━━━━━━━━━━━━
{} di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Mudah dan AMAN!
━━━━━━━━━━━━━━━━━━━━━━━━
Jika anda Tidak Mempercayai Bot ini:
1. Jangan dibaca Pesan ini
2. Hapus Pesan dan Blokir Bot ini
━━━━━━━━━━━━━━━━━━━━━━━━
Managed With ☕️ By @MSDZULQURNAIN**
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
