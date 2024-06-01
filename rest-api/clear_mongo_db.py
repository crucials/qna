from src.mongo_database import main_database


for collection in main_database.list_collection_names():
    delete_result = main_database.get_collection(collection).delete_many({})
    print(f'deleted {delete_result.deleted_count} docs from \'{collection}\'')
