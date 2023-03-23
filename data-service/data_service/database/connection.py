import os
from typing import Optional
from pymongo import MongoClient
from pymongo.server_api import ServerApi

DB_CLIENT: Optional[MongoClient] = None


def get_db_client():
    global DB_CLIENT
    connection_str = os.getenv("DB_URL")
    if connection_str is None:
        raise ValueError("DB_URL environment variable not set.")
    if DB_CLIENT is None:
        DB_CLIENT = MongoClient(
            connection_str,
            server_api=ServerApi("1"),
        )
    return DB_CLIENT


def get_db(db_name: Optional[str] = None):
    db = db_name if db_name is not None else os.getenv("DB_NAME")
    if db is None:
        raise ValueError("DB_NAME environment variable not set.")
    client = get_db_client()
    return client[db]
