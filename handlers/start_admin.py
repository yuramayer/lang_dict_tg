"""Bot reacts to the command /start for the admins"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from filters.admin_checker import IsAdmin
from config.conf import admins_ids


start_admin_router = Router()
start_admin_router.message.filter(
    IsAdmin(admins_ids)
)


@start_admin_router.message(Command('start'))
async def cmd_start(message: Message):
    """Bot says hi to the admins"""
    await message.answer('Работает :)')
