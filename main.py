import os
import time

import pymongo
import re
from misc import personMaster

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imaginaryMaster"]
mycol = mydb["people"]
dbCurs = mycol.find({})


def enter_to_continue():
    print("", flush=True)
    input("Press enter to continue...")


def generate_people():
    while True:
        tab_down()
        usr_sel = input(" Amount of people to generate(integer) >> ")
        try:
            usr_sel = int(usr_sel)

            for person in range(0, usr_sel):
                person = personMaster()
                mycol.insert_one(person.__dict__)
            print(
                f"Generated '{usr_sel}' identities and successfully inserted those to the register and external database.")
            break
        except:
            print("Please enter a valid positive, integer number...")
            pass
    time.sleep(2)


def fuzzy_matching():
    res = mycol.find({"$text": {"$search": "Thoma"}})
    print(list(res))

fuzzy_matching()


def search():
    while True:
        clear()
        tab_down()
        print(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
              f"-  |   Identity Search  | -\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
              f"-    [1]- First Name      -\n"
              f"+    [2]- Last Name       +\n"
              f"-    [3]- P'IdentNum      -\n"
              f"+    [4]- Eye Colour      +\n"
              f"-    [5]- Height          -\n"
              f"+    [6]- Nationality     +\n"
              f"-    [7]- Age             -\n"
              f"+                         +\n"
              f"-      [ E/e(Exit) ]      -\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        tab_down()
        usr_sel = input(" >> ")
        if usr_sel.lower().strip(" ") == "e":
            break
        elif usr_sel.lower().strip(" ") == "1":
            # First_name Search
            usr_sel = input(" Name >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'first_name': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "2":
            # Last_name search
            usr_sel = input(" Surname >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'last_name': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "3":
            # Personal Identification Number search
            usr_sel = input(" Personal Identification Number (ex. 19990101-9984) >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'personal_identification_number': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "4":
            # Eye Colour Search
            usr_sel = input(" Eye Colour >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'eye_colour': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "5":
            # Height Search
            print("[Currently under maintenance, No results will be returned. Please check back later or contact the "
                  "administration for further "
                  "instructions...]")
            usr_sel = input(" Height(cm) >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                dbCurs = mycol.find({"height": f"{int(usr_sel)}"})

        elif usr_sel.lower().strip(" ") == "6":
            # Nationality search
            usr_sel = input(" Nationality >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'nationality': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        else:
            pass

        tab_down()
        line()
        for i in dbCurs:
            print(
                f"{i.get('first_name')} {i.get('last_name')}, {i.get('age')} y/o, {i.get('height')}cm, {i.get('nationality')}, ({i.get('personal_identification_number')})")
            line()
        enter_to_continue()
        

def line():
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def list_people():
    # List all people
    for document in dbCurs:
        print(
            f"{document.get('first_name')} {document.get('last_name')}, {document.get('age')} y/o, {document.get('height')}cm, {document.get('nationality')}.")


def tab_down():
    print()


def get_statistics(selection: int):
    if selection == 1:
        total_in_database = mydb.command("count", "people")
        return total_in_database


def main():
    clear()
    while True:
        clear()
        print(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
              f"-  G/g(Generate People)   -\n"
              f"+  L/l(List Register)     +\n"
              f"-  S/s(Search)            -\n"
              f"+                         +\n"
              f"-                         -\n"
              f"+      [ E/e(Exit) ]      +\n"
              f"-                         -\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
              f"In register:{get_statistics(1)}")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("g"):
            # Generate
            generate_people()

        elif usr_sel.__contains__("l"):
            # List
            list_people()

        elif usr_sel.__contains__("s"):
            search()

        elif usr_sel.__contains__("e"):
            # Exit
            print("Exiting...")
            exit(0)


if __name__ == '__main__':
    main()
