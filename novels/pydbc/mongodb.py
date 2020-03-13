import pymongo


class MongoDBNovel:
    def __init__(self):
        self.uri = 'localhost'
        self.port = 27017

    def start_connection(self, collection):
        self.client = pymongo.MongoClient(self.uri, self.port)
        self.db = self.client['NovelBase']
        self.collection = self.db[collection]

    def query(self, query,**kwargs):
        if self.collection.count_documents(query)>0:
            if kwargs:
                return self.collection.find(query,kwargs)
            else:
                return self.collection.find(query)
        else:
            return

    def close_connection(self):
        self.client.close()
