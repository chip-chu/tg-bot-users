import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

from utils.validate_values import validate_env_values

if not find_dotenv():
    exit('Переменные окружения не загружены')
else:
    load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
BOT_TOKEN = os.getenv('BOT_TOKEN')
COMMANDS = (
    ('anniversary_list', "Получить не поздравленных пользователей"),
    ('users_history', "Показать историю поздравленных\не поздравленных"),
)

USER_THRESHOLD, ADMINISTRATORS_GROUP_ID, USERS_GROUP = validate_env_values()
