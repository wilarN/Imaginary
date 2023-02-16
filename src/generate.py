import json

from pymongo import MongoClient

from src.headers import *
import src.searches
import pymongo

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["imaginaryMaster"]
mycol = mydb["people"]
mycolVehicle = mydb["vehicles"]
mycolBank = mydb["banking"]
global dbCurs
dbCurs = mycol.find({})


def generate_people():
    global mycol
    while True:
        src.headers.tab_down()
        usr_sel = input(" Amount of people to generate(integer) >> ")
        try:
            usr_sel = int(usr_sel)

            for person in range(0, usr_sel):
                person = src.misc.personMaster()
                person_dict = person.__dict__
                person_dict["bank_accounts"] = [account.__dict__ for account in person.bank_accounts]
                person_name_full = str(person.first_name + " " + person.last_name)
                # generate_banking_account_for_person(accounts=person.bank_accounts, owner=person_name_full)
                mycol.insert_one(person_dict)
            print(
                f"Generated '{usr_sel}' identities and successfully inserted those to the register and external "
                f"database.")
            break
        except Exception as e:
            print(e)
            print("Please enter a valid positive, integer number...")
            pass
    time.sleep(2)


def generate_vehicle(specific_plate=None, ownership=None):
    global mycolVehicle
    if specific_plate is None:
        while True:
            # tab_down()
            usr_sel = input(" Amount of vehicles to generate(integer) >> ")
            try:
                usr_sel = int(usr_sel)

                for vehicle in range(0, usr_sel):
                    vehicle = src.misc.carMaster()
                    mycolVehicle.insert_one(vehicle.__dict__)
                print(
                    f"Generated '{usr_sel}' vehicles and successfully inserted those to the register and external "
                    f"database.")
                break
            except Exception as e:
                print(e)
                print("Please enter a valid positive, integer number...")
        time.sleep(2)
    else:
        vehicle = src.misc.carMaster(spec_plate=specific_plate, owner=ownership)
        mycolVehicle.insert_one(vehicle.__dict__)
        return vehicle


def generate_banking_account_for_person(accounts, owner):
    global mycolBank
    try:
        for account in accounts:
            mycolBank.insert_one(account)
        print(f"Generated banking account for {owner}")
    except Exception as e:
        print(e)
        print("Please try again later...")
