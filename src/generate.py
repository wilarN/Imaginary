from src.headers import *
import src.searches

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imaginaryMaster"]
mycol = mydb["people"]
mycolVehicle = mydb["vehicles"]
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
                mycol.insert_one(person.__dict__)
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
                pass
        time.sleep(2)
    else:
        vehicle = src.misc.carMaster(spec_plate=specific_plate, owner=ownership)
        mycolVehicle.insert_one(vehicle.__dict__)
        return vehicle