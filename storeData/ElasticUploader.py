from Elastic_service.DAL import DAL ,ConnES

class ElasticUploader:
    def __init__(self, host, index):
        self.dal = DAL(index,create_index=True)
    def upload_metadata(self, metadata):
        self.dal.insert_data(metadata)

