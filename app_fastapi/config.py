import os
from dotenv import load_dotenv

load_dotenv()  # Извлекаем переменные окружения из файла .env

# BOT
TOKEN = os.environ.get("TOKEN")

# PostgresSQL
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# REDIS
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_NUM_DB = os.environ.get("REDIS_NUM_DB")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_NUM_DB}'
