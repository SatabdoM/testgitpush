import pymongo

client = pymongo.MongoClient("mongodb+srv://SatabdoM:Rockandroll77@cluster0.eeb09.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}
d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}
d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}
d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}
d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}d={
    "name":"satabdo",
    "email":"satabdomajumdar@gmail.com",
    "surname":"majumder"
}
db1=client['mongotest']
coll=db['test']

coll.insert_one(d)