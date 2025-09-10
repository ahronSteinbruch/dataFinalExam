from utils.mongo_servise.crud import MongoCRUD

class MongoUploader:
    def __init__(self, uri, db, collection):
        self.mongo = MongoCRUD(uri, db, collection)

    def upload_file(self, file_path, file_hash):
        self.mongo.insert_file(file_path, file_hash)

