from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    """
**Halo 
━━━━━━━━━━━━━━━━━━━━━━━━
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ᴘʀᴇᴍɪᴜᴍ💎
├ ʀᴘ. 30.000  [ ᴘᴇʀʙᴜʟᴀɴ ]
├ ᴅᴇᴘʟᴏʏ ᴅɪ ʜᴇʀᴏᴋᴜ
├ ꜰᴜʟʟ ɢᴀʀᴀɴꜱɪ 1 ʙᴜʟᴀɴ
└ sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ
━━━━━━━━━━━━━━━━━━━━━━━━
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ʙɪᴀsᴀ🤖
├ ʀᴘ. 20.000  [ ᴘᴇʀʙᴜʟᴀɴ ]
├ ᴅᴇᴘʟᴏʏ ᴅɪ ʜᴇʀᴏᴋᴜ
├ ꜰᴜʟʟ ɢᴀʀᴀɴꜱɪ 1 ʙᴜʟᴀɴ
└ sɪsᴛᴇᴍ ᴛᴇʀɪᴍᴀ ᴊᴀᴅɪ
━━━━━━━━━━━━━━━━━━━━━━━━
Hubungi admin dibawah untuk melakukan transaksi & acc**""",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ADMIN", url="https://t.me/MSDZULQRNN")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Kamu bukan admin!")
