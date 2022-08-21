import pymongo
client = pymongo.MongoClient("mongodb+srv://srwshhv2:Mongodb123@cluster0.4zdaegu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"Serwesh",
    "enail":"abc@gmail.com",
    "surname":"kumar"
}

d1={
    "name":"ajith",
    "enail":"abc@gmail.com",
    "surname":"kumar"
}
db1=client['mongodbtest']
coll=db1['test']
coll.insert_one(d)
coll.insert_one(d1)
