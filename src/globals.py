import os
import time
import datetime

from pymongo import MongoClient
global myclient

address = "localhost"
port = "27017"

def graceful_exit():
    # Exit
    print("Exiting...")
    file = open(settings_file_location, "a+")
    file.write(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
               f"[{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] (EXITING...)\n"
               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    file.close()
    exit(0)


try:
    myclient = MongoClient(f"mongodb://{address}:{port}/")
except Exception as e:
    print(e)
    print("Connection to database failed. Please make sure the database is fully functional and up and running!")
    time.sleep(2)
    graceful_exit()

mydb = myclient["imaginaryMaster"]
mycol = mydb["people"]
mycolVehicle = mydb["vehicles"]
mycolBank = mydb["banking"]
dbCurs = mycol.find({})


settings_file_location = os.path.join(os.path.dirname(__file__), "../" + 'global.log')
