"""Methods working with bot's text"""


def create_words_message(
        relevant_words: dict) -> str:
    """Creates pretty text for the message"""

    txt = '📖 Подходящие слова:\n\n'

    for key, value in relevant_words.items():
        txt += f' - <b>{key}</b> - {value}\n'

    return txt


def check_word_message(
        word: str, translation: str) -> str:
    """Creates pretty text for checking the new word"""

    txt = (
        '🔖 Ты сохраняешь новую пару:\n\n'
        f'<b>{word}</b> - <b>{translation}</b>'
        '\n\nВсё верно?'
    )

    return txt


def create_start_message() -> str:
    """Creates start message describing the bot"""

    txt = (
        'Я помогаю хранить и вспоминать иностранные слова 📗\n\n'
        'У меня есть 3 команды:\n'
        '  👉🏻 <b>/add_word</b> - сохрани новую фразу в словарь\n'
        '  👉🏾 <b>/get_word</b> - найди нужную фразу в словарике\n'
        '  👉🏼 Нажми <b>/cancel</b> чтобы отменить любую операцию\n\n'
        'Пока твой словарь пустой, добавь первое слово'
        'с помощью /add_word 😉\n\n'
        '\n\nБудут вопросы - обращайся <b>@botrqst</b>'
    )

    return txt


def create_end_message() -> str:
    """Created the message sending in the end of the operations"""

    txt = (
        'Чем ещё могу помочь?\n\n'
        '  👉🏻 <b>/add_word</b> - добавить новое слово\n'
        '  👉🏾 <b>/get_word</b> - найти фразу в словаре\n'
    )

    return txt
