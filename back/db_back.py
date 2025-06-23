"""Methods for the sqlite database"""

import sqlite3
from config.conf import DB_PATH


def user_exists(chat_id: str) -> bool:
    """Check if a user exists in the users table.

    Args:
        chat_id (str): Telegram chat ID of the user.

    Returns:
        bool: True if user exists, False otherwise.
    """
    query = 'SELECT 1 FROM users WHERE chat_id = ? LIMIT 1'
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (chat_id,))
            return cursor.fetchone() is not None
    except sqlite3.Error as error:
        print(f'Error checking user: {error}')
        return False


def add_user(chat_id: str) -> None:
    """Add a new user to the users table.

    Args:
        chat_id (str): Telegram chat ID of the user.
    """
    query = 'INSERT OR IGNORE INTO users (chat_id) VALUES (?)'
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (chat_id,))
            conn.commit()
    except sqlite3.Error as error:
        print(f'Error adding user: {error}')


def get_user_dict(chat_id: str) -> dict[str, str] | None:
    """Get all word-translation pairs for a user as a dictionary.

    Args:
        chat_id (str): Telegram chat ID of the user.

    Returns:
        dict[str, str] | None: Dictionary of word: translation pairs,
            or None if an error occurs or user not found.
    """
    query = """
        SELECT d.word, d.translation
        FROM dicts d
        JOIN users u ON d.user_id = u.id
        WHERE u.chat_id = ?
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (chat_id,))
            result = cursor.fetchall()
            return {word: translation for word, translation in result}
    except sqlite3.Error as error:
        print(f'Error getting user dict: {error}')
        return None


def add_word_for_user(chat_id: str,
                      word: str,
                      translation: str) -> None:
    """Add a new word-translation pair for the user.

    Args:
        chat_id (str): Telegram chat ID of the user.
        word (str): The word to add.
        translation (str): The translation of the word.
    """
    get_user_id_query = 'SELECT id FROM users WHERE chat_id = ?'
    insert_word_query = '''
        INSERT INTO dicts (user_id, word, translation)
        VALUES (?, ?, ?)
    '''
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(get_user_id_query, (chat_id,))
            row = cursor.fetchone()
            if row is None:
                print(f'User with chat_id {chat_id} not found.')
                return
            user_id = row[0]
            cursor.execute(insert_word_query, (user_id, word, translation))
            conn.commit()
    except sqlite3.Error as error:
        print(f'Error adding word: {error}')
