import pymongo
import time
from pymongo import MongoClient
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://Felicia:B10815009@cluster0.oqz45.mongodb.net/Hope?retryWrites=true&w=majority")
db = client["Hope"]

#Auction
table = db["Auction"]
print("Ongoing Auctions:")
res = table.find({},{"_id":0})
rep = 0
for x in res:
    print(rep," ",x["Title"])
    rep=rep+1
print("Input the title of the Auction that will be deleted!")
selected = input()
rep = 0
res = table.find({},{"_id":0})
for x in res:
    if selected == str(x["Title"]):
        print("Are you sure? (Y/N)")
        ans = input()
        if ans == "Y":
            table.delete_one({"Title":selected})
    else:
        rep = rep+1
if rep == table.count_documents({}):
    print("Title not Found!")
print("\nCurrent Data")
res = table.find({},{"_id":0})
rep = 0
for x in res:
    print(rep," ",x)
    rep=rep+1


#Fund Raising
print("\n")
table = db["Fund Raising"]
print("Ongoing Fund Raisings:")
res = table.find({},{"_id":0})
rep = 0
for x in res:
    print(rep," ",x)
    rep=rep+1
print("Input the title of the Fund Raising that will be deleted!")
selected = input()
rep = 0
res = table.find({},{"_id":0})
for x in res:
    if selected == str(x["Title"]):
        print("Are you sure? (Y/N)")
        ans = input()
        if ans == "Y":
            table.delete_one({"Title":selected})
    else:
        rep=rep+1
if rep == table.count_documents({}):
    print("Title not Found!")
print("\nCurrent Data")
res= table.find({},{id:0})
rep=0
for x in res:
    print(rep," ",x)
    rep=rep+1
