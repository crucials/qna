import os

from dotenv import load_dotenv
from pymongo import MongoClient, TEXT


load_dotenv()

client = MongoClient(os.environ.get('MONGO_DB_CONNECTION_STRING'))
main_database = client.get_database('main')

accounts_collection = main_database.get_collection('accounts')
accounts_collection.create_index(
    {
        'name': TEXT,
    },
    unique=True
)

questions_collection = main_database.get_collection('questions')
