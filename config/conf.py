"""Loading the environment keys for the project"""

import os
from dotenv import load_dotenv


load_dotenv()


def get_checked_env(env_name):
    """Environment checker"""
    env = os.getenv(env_name)
    if not env:
        raise RuntimeError(f"The required variable isn't defined: {env_name}")
    return str(env)


OPENAI_TOKEN = get_checked_env('OPENAI_TOKEN')
TEST_BOT_TOKEN = get_checked_env('TEST_BOT_TOKEN')
PROD_BOT_TOKEN = get_checked_env('PROD_BOT_TOKEN')
DB_PATH = get_checked_env('DB_PATH')
ADMINS = get_checked_env('ADMINS')
STAND = str(os.getenv('STAND'))

if STAND == 'LOCAL':
    BOT_TOKEN = TEST_BOT_TOKEN
elif STAND == 'PROD':
    BOT_TOKEN = PROD_BOT_TOKEN

admins_ids = [int(admin_id) for admin_id in ADMINS.split(',')]
