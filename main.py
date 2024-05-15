import logging
import asyncio
from aiogram.enums import ParseMode
import sys
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command
from aiogram.methods.delete_webhook import DeleteWebhook
from aiogram.utils.markdown import hlink
from aiogram.client.bot import DefaultBotProperties
from plyer import notification
from config import *

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()

# insert a list with the id of users who can set reminders
allowed_id = [1223353442]

@dp.message()
async def remind(message: types.Message):
    if message.from_user.id in allowed_id:
        notification.notify(title="mbutsk's reminder", message=message.text)
        await message.reply(f'You should have received a reminder with the message "{message.text}"')
    else:
        await message.reply(f'The message "{message.text}" has not arrived. You do not have permission to send reminders to this user.'
                            f'{hlink("Get mbutsk's reminder to yourself", "https://github.com/mbutskpy/mbutsks-reminder")}')

async def main() -> None:
    await bot(DeleteWebhook(drop_pending_updates=False))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())