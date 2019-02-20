import pymongo
from pymongo import MongoClient


class ToRegister:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        id = self.Users.insert_one({"username": data.username, "name": data.name, "email": data.email, "password": data.password})
        self.Users.insert_one({"username": data.username, "name": data.name, "email": data.email, "password": data.password})
        print("your id is", id)
