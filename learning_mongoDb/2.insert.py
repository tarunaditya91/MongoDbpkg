import pymongo 

if __name__=="__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db=client["Tarun"]
    collection=db['my sample collection ']
    dictionary={'name':"tarun aditya",'mark':45}
    # collection.insert_one(dictionary)
    insert_list=[
        {'name':"tarun aditya",'mark':56,'age':'21'},
        {'name':"tarun aditya",'mark':56,'age':'21'},
        {'name':"tarun aditya",'mark':56,'age':'21'},
        {'name':"tarun aditya",'mark':56,'age':'21'}
    ]
    collection.insert_many(insert_list)
