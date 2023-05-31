from telethon import TelegramClient
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

from data import Data


ask_ques = "**SILAKAN PILIH STRING YANG MAU LU AMBIL**"
buttons_ques = [
    [
        InlineKeyboardButton("PYROGRAM V2", callback_data="pyrogram"),
        InlineKeyboardButton("TELETHON", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("PYROGRAMV2 BOT", callback_data="pyrogram_bot"),
        InlineKeyboardButton("TELETHON BOT", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"Mulai mengambil string {ty}...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Tolong kirimkan `API_ID`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('API_ID tidak cocok (silakan cek kembali). Dan coba mulai mengambil ulang klik /start', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, 'Tolong kirimkan `API_HASH`', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "Tolong kirimkan `PHONE_NUMBER` sesuai kode negara mu. \nContoh : `+19876543210`'"
    else:
        t = "Tolong kirimkan `BOT_TOKEN` di akun mu \nContoh : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("Sedang mengirim OTP...")
    else:
        await msg.reply("Sedang login ke bot kamu..")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name=f"bot_{user_id}", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    else:
        client = Client(name=f"user_{user_id}", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` dan `API_HASH` Tidak cocok. Tolong mulai mengambil ulang klik /start', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` Tidak cocok. Tolong mulai mengambil ulang klik /start', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "Silakan cek kode OTP di akunmu...\n**Kirimkan kode dengan spasi Contoh** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('Waktu habis dalam 10 menit. Tolong mulai mengambil ulang klik /start.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply('OTP tidak cocok. Tolong mulai mengambil ulang klik /start', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply('OTP Kadaluwarsa. Tolong mulai mengambil ulang klik /start', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError):
            try:
                two_step_msg = await bot.ask(user_id, 'Akunmu terpasang two-step verification. Tolong kirimkan password nya...', filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('Waktu habis dalam 5 menit. Tolong mulai mengambil ulang klik /start', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError):
                await two_step_msg.reply('Password tidak cocok. Tolong mulai mengambil ulang klik /start', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**KIRIMKAN STRING SESSION KE @DZuserbot** \n\n`{string_session}`"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "Silakan cek di PESAN TERSIMPAN dan kirimkan string session di sini untuk mengaktifkan 𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Proses dibatalkan!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Restart bot!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Pengambilan string dibatalkan!", quote=True)
        return True
    else:
        return False
