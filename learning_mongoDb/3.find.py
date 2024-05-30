import pymongo 

if __name__=="__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db=client["Tarun"]
    collection=db['my sample collection ']
    dictionary={'name':"tarun aditya",'mark':45}
    # find1=collection.find()
    findall=collection.find({'name':"tarun aditya"})

    for i in findall:
        print(i)
    
    findallq=collection.find({'name':"tarun aditya"},{'mark':1,'_id':0})
    for i in findallq:
        print(i)
