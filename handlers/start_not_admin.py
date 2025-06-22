"""Bot reacts to the command /start for the others"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from filters.admin_checker import IsAdmin
from config.conf import admins_ids


start_not_admin_router = Router()
start_not_admin_router.message.filter(
    IsAdmin(admins_ids)
)


@start_not_admin_router.message(Command('start'))
async def cmd_start_not_admin(message: Message):
    """Not admins want to use the bot"""
    await message.answer('Это частный бот')
