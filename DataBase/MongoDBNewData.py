import pymongo
import time
from pymongo import MongoClient
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://Felicia:B10815009@cluster0.oqz45.mongodb.net/Hope?retryWrites=true&w=majority")
db = client["Hope"]

#Auction
table = db["Auction"]

print("Title:")
title = input()
print("Explanation:")
explain = input()
print("Picture Link:")
piclink = input()

post = {"Title": title, "Explanation":explain, "Date Created":datetime.utcnow(),"Highest Value": 0, "Highest Bidder": "-", "Picture": piclink, "Available": True,
        "Transaction":{"Winner":"-", "Amount": 0, "Date":datetime.utcnow()}}
table.insert_one(post)
res = table.find({"Available":True},{"_id":0})
rep = 0
print("Ongoing Auctions:\n")
for x in res:
    print(rep," ",x)
    rep=rep+1

#Fund Raising

print("\n")
table = db["Fund Raising"]

print("Title:")
title = input()
print("Explanation:")
explain = input()
print("Receiver:")
receiver = input()
print("Picture Link:")
piclink = input()
post = {"Title" : title, "Explanation":explain, "Data Created": datetime.utcnow(), "Total Amount": 0, "Receiver": receiver, "Picture":piclink, "Transactions":{}}

#Username
table = db["Personal Info"]
print("Username:")
username = input()
print("Password:")
password = input()
print("Email:")
email = input()
post = {"Username":str(username),"Password":str(password),"Email":str(email),"Date Created":datetime.utcnow(), "Current Amount":0, "Transaction":{}}
table.insert_one(post)
print("New Username Created")