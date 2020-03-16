from novels.pydbc.mongodb import MongoDBNovel

mongodb = MongoDBNovel()

mongodb.start_connection(collection='novels')

if __name__ == '__main__':
    query ={'No':'35922'}
    novels = mongodb.query(query,link=1)
    if novels:
        print(novels[0])