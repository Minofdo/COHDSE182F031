import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["login"]

user_name = input("Enter user name : ")
password = input("Enter password : ")
for x in collection.find({},{"userName":1,"password":1}):
    name=str(x["userName"])
    password=str(x["password"])

if user_name==name and password==password:
    print("login successful")

else:
        print("login failed")

    
