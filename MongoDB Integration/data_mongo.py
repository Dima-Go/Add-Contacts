import pymongo
from bson import ObjectId
from dotenv import load_dotenv
import os
import uuid
load_dotenv()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["contacts_app2"]
mycol = mydb["contacts"]

def get_contacts():
    return list(mycol.find())

def findByNumber(_id):
    return mycol.find_one({"_id": ObjectId(_id)})

def search_contacts(name):
    query = {"name": {"$regex": name, "$options": "i"}}
    return list(mycol.find(query))

def contact_exists(fullname, email):
    query = mycol.find_one({"$or": [{"name": fullname}, {"email": email}]}) 
    return bool(query)

def create_contact(name, phone, email, gender, photo):
    mycol.insert_one(
        {"name": name, "phone": phone, "email": email, "gender": gender, "photo": photo})
    return "Contact added successfully"

def delete_contact(_id):
    query = mycol.delete_one({"_id": ObjectId(_id)})
    return f"{query.deleted_count} was deleted from Contacts"

def update_contact(_id, name, phone, email, gender):
    mycol.update_one(
        {"_id": _id}, 
        {"$set": {"name": name, "phone": phone, "email": email, "gender": gender}} 
    )