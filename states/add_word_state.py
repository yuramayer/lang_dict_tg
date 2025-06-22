"""State for adding the new word to the dict"""

# pylint: disable=too-few-public-methods

from aiogram.fsm.state import StatesGroup, State


class AddWord(StatesGroup):
    """New page State: add the word to the dict"""
    add_word = State()
    approved = State()
