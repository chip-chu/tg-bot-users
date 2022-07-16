import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import sqlite3


if not find_dotenv():
    exit('Переменные окружения не загружены')
else:
    load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
BOT_TOKEN = os.getenv('BOT_TOKEN')
COMMANDS = (
    ('help', "Вывести справку"),
)


USER_THRESHOLD = 4
ADMINISTRATORS_GROUP_ID = os.getenv('ADMINISTRATORS_GROUP_ID')
USERS_GROUP = os.getenv('USERS_GROUP')
