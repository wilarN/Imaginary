from pymongo import MongoClient
global myclient
myclient = MongoClient("mongodb://localhost:27017/")
global mydb
mydb = myclient["imaginaryMaster"]
global mycol
mycol = mydb["people"]
global mycolVehicle
mycolVehicle = mydb["vehicles"]
global mycolBank
mycolBank = mydb["banking"]
global dbCurs
dbCurs = mycol.find({})
