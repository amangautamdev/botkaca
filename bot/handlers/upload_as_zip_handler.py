from pyrogram import Client
from pyrogram.filters import Filters
from pyrogram.types import Message
from bot import LOCAL, STATUS, COMMAND

@Client.on_message(Filters.command(COMMAND.UPLOAD_AS_ZIP))
async def func(client : Client, message: Message):
    STATUS.UPLOAD_AS_ZIP = not STATUS.UPLOAD_AS_ZIP
    await message.reply_text(LOCAL.UPLOAD_AS_ZIP.format(status=STATUS.UPLOAD_AS_ZIP))
