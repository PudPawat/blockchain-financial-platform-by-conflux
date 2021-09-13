import pymongo
import time
from pymongo import MongoClient
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://Felicia:B10815009@cluster0.oqz45.mongodb.net/Hope?retryWrites=true&w=majority")
db = client["Hope"]

#Auction
table = db["Auction"]
table.delete_many({})

#Fund Raising
table = db["Fund Raising"]
table.delete_many({})