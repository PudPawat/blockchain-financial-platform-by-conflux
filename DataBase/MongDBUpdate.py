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
print("Please input the title of the auction that will be updated!")
selected = input()
rep = 0
res = table.find({},{"_id":0})
for x in res:
    if selected == str(x["Title"]):
        print("Which data will be updated?")
        update = input()
        if update == "Title":
            print("Please input the updated Title!")
            title = input()
            table.update_one({"Title": selected}, {"$set": {"Title": title}})
        elif update == "Explanation":
            print("Please input the updated Explanation!")
            explain = input()
            table.update_one({"Title": selected}, {"$set": {"Explanation": explain}})
        elif update == "Picture":
            print("Please input the new Picture Link!")
            piclink = input()
            table.update_one({"Title": selected}, {"$set": {"Picture": piclink}})
        elif update == "New Bid":
            print("Please enter the new value!")
            currentbid = input()
            topbid = table.find_one({"Title": selected})
            if topbid["Highest Value"] < int(currentbid):
                print("Your bid is accepted! Please input your name!")
                name = input()
                table.update_one({"_id": topbid["_id"]},
                                 {"$max": {"Highest Value": int(currentbid)}, "$set": {"Highest Bidder": name}})
            else:
                print("Your bid is lower than the current bid!")
        else:
            print("Input doesn't match!")
    else:
        rep = rep+1
if table.count_documents({}) == rep:
    print("Title not found!")
print("\nCurrent Data")
res = table.find({"Available":True},{"_id":0, "Date Created":0, "Transaction":0})
rep = 0
for x in res:
    print(rep," ",x)
    rep=rep+1

#Fund Raising
print("\n")
table = db["Fund Raising"]
res = table.find({},{"_id":0})
rep = 0
for x in res:
    print(rep," ",x["Title"])
    rep=rep+1
print("Please input the title Fund Raising that will be updated!")
selected = input()
rep = 0
res = table.find({}, {"_id":0})
for x in res:
    if selected == str(x["Title"]):
        print ("Which data will be updated?")
        update = input()
        if update =="Title":
            print("Please input the updated Title!")
            title=input()
            table.update_one({"Title":selected},{"$set":{"Title":title}})
        elif update == "Explanation":
            print ("Please input the updated Explanation!")
            explanation = input()
            table.update_one({"Title": selected}, {"$set":{"Explanation":explain}})
        elif update == "Picture":
            print("Please input the new Picture link!")
            pict = input()
            table.update_one({"Title":selected}, {"$set":{"Picture":pict}})
        elif update == "New Transaction":
            print ("Please input your name!")
            name = input()
            print("Please input your amount!")
            amount = input()
            table.update_one({"Title":selected}, {"$push":{"Transactions":{"From":name, "Amount":int(amount), "Date Created":datetime.utcnow()}},"$inc":{"Total Amount":int(amount)}}) #inc means total amount+amount that newly inputted
        else:
            print("Input doesn't match!")
    else:
        rep = rep+1
if table.count_documents({}) == rep:
    print("Title not found!")
print("\nCurrent Data")
res = table.find({"Available": True},{"_id":0, "Date Created":0, "Transactions":0})
rep = 0
for x in res:
    print(rep," ",x) # x = data
    rep = rep + 1