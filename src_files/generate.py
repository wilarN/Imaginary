import json

from pymongo import MongoClient
import src_files.globals as glob
from src_files.headers import *
import src_files.searches
import pymongo
global mycol
global mycolVehicle
global mycolBank

def generate_people():
    while True:
        tab_down()
        usr_sel = input(" Amount of people to generate(integer) >> ")
        try:
            usr_sel = int(usr_sel)

            for person in range(0, usr_sel):
                person = src_files.misc.personMaster()
                person_dict = person.__dict__
                person_dict["bank_accounts"] = [account.__dict__ for account in person.bank_accounts]
                person_name_full = str(person.first_name + " " + person.last_name)
                # generate_banking_account_for_person(accounts=person.bank_accounts, owner=person_name_full)
                glob.mycol.insert_one(person_dict)
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
    if specific_plate is None:
        while True:
            # tab_down()
            usr_sel = input(" Amount of vehicles to generate(integer) >> ")
            try:
                usr_sel = int(usr_sel)

                for vehicle in range(0, usr_sel):
                    vehicle = src_files.misc.carMaster()
                    glob.mycolVehicle.insert_one(vehicle.__dict__)
                print(
                    f"Generated '{usr_sel}' vehicles and successfully inserted those to the register and external "
                    f"database.")
                break
            except Exception as e:
                print(e)
                print("Please enter a valid positive, integer number...")
        time.sleep(2)
    else:
        vehicle = src_files.misc.carMaster(spec_plate=specific_plate, owner=ownership)
        glob.mycolVehicle.insert_one(vehicle.__dict__)
        return vehicle


def generate_banking_account_for_person(accounts, owner):
    try:
        for account in accounts:
            glob.mycolBank.insert_one(account)
        print(f"Generated banking account for {owner}")
    except Exception as e:
        print(e)
        print("Please try again later...")
