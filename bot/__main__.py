from os.path import join as os_path_join
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from bot import CONFIG, COMMAND, LOCAL, LOGGER, STATUS
from bot.handlers import *
import asyncio

async def main():
    # Initialize bot
    app = Client(
        "Bot",
        bot_token=CONFIG.BOT_TOKEN,
        api_id=CONFIG.API_ID,
        api_hash=CONFIG.API_HASH,
        workdir=os_path_join(CONFIG.ROOT, CONFIG.WORKDIR),
        plugins=dict(root="bot/handlers")
    )
    app.set_parse_mode("html")

    # Register /start handler
    app.add_handler(
        MessageHandler(
            start_message_handler.func,
            filters=filters.command(COMMAND.START)
        )
    )

    if CONFIG.BOT_PASSWORD:
        # Register /pass handler
        app.add_handler(
            MessageHandler(
                password_handler.func,
                filters=filters.command(COMMAND.PASSWORD)
            )
        )

        # Take action on unauthorized chat room
        app.add_handler(
            MessageHandler(
                wrong_room_handler.func,
                filters=lambda msg: msg.chat.id not in STATUS.CHAT_ID
            )
        )

    # Start the bot
    await app.start()

if __name__ == '__main__':
    asyncio.run(main())
