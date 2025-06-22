"""Module with ChatGPT functions"""

from openai import OpenAI
from config.conf import OPENAI_TOKEN


client = OpenAI(api_key=OPENAI_TOKEN)


def find_relevant_words(
        user_dict: dict[str, str], query: str
        ) -> list[str]:
    """Find user words semantically relevant to a query using OpenAI API

    Args:
        user_dict (dict): Dictionary of {word: translation}.
        query (str): User query, e.g. 'кушать'.

    Returns:
        list[str]: List of relevant user words (keys from user_dict).
    """

    prompt = (
        "Ты работаешь в словарном помощнике.\n"
        "Вот список слов, которые пользователь уже знает:\n\n"
        f"{', '.join(user_dict.keys())}\n\n"
        "Запрос пользователя: " + query + "\n\n"
        "Найди 10 слов из его словаря,"
        "которые ближе всего по смыслу или теме к запросу.\n"
        "Отвечай только списком слов через запятую, без номеров и пояснений.\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system",
                 "content": "Ты — помощник по изучению языка."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        raw_text = response.choices[0].message.content.strip()
        return [word.strip() for word in raw_text.split(",")
                if word.strip() in user_dict]

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return []
