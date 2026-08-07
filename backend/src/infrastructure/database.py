# infrastructure/database.py

from config import Config
from database import Database

database = Database(
    Config.DATABASE_URL
)