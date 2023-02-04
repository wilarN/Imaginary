import os
import time

import pymongo
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


def search():
    while True:
        clear()
        tab_down()
        print(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
              f"-     Identity Search     -\n"
              f"+                         +\n"
              f"-      [ E/e(Exit) ]      -\n"
              f"+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        tab_down()
        usr_sel = input(" Name >> ")
        usr_sel = usr_sel.strip(" ").capitalize()
        if usr_sel.lower().strip(" ") == "e":
            break
        else:
            name_query = {"first_name": f"{usr_sel}"}
            curs = mycol.find(name_query)
            tab_down()
            line()
            for i in curs:
                print(
                    f"{i.get('first_name')} {i.get('last_name')}, {i.get('age')} y/o, {i.get('height')}cm, {i.get('nationality')}, ({i.get('personal_identification_number')})")
                line()
            del curs
            enter_to_continue()


def line():
    print("===============================================================")


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
