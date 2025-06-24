"""Bot reacts to the command /start for the admins"""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters.admin_checker import IsAdmin
from config.conf import admins_ids
from back.bot_back import create_end_message


cancel_router = Router()
cancel_router.message.filter(
    IsAdmin(admins_ids)
)


@cancel_router.message(Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext):
    """User cancels the current state"""
    await state.clear()
    await message.answer('Операция отменена 👌🏻')
    end_msg = create_end_message()
    await message.answer(end_msg)
