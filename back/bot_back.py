"""Methods working with bot's text"""


def create_words_message(
        relevant_words: dict) -> str:
    """Creates pretty text for the message"""

    txt = '📖 Подходящие слова:\n\n'

    for key, value in relevant_words.items():
        txt += f' - <b>{key}</b> - {value}\n'

    return txt
