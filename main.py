from datetime import datetime

import src.searches

from src.headers import *
import src.globals

"""
IMPORTANT NOTICE: This program is provided for educational and experimental purposes only. The creator of this 
program is not responsible for any damages or losses caused by the use of this program. Use this program at your own 
risk. OBS! This program is provided as is and for educational purposes only. It is not intended to be used for any 
malicious or illegal activities. The user assumes all responsibility for any use of this program. The creator of this 
program shall not be held responsible for any consequences or damages resulting from the use of this program for any 
purpose.
"""


def change_windowSize():
    cmd = "mode con: cols=230 lines=50"
    os.system(cmd)

def list_people():
    # List all people
    for document in dbCurs:
        print(
            f"{document.get('first_name')} {document.get('last_name')}, {document.get('age')} y/o, {document.get('height')}cm, {document.get('nationality')}.")


def get_statistics(selection: int):
    if selection == 1:
        total_in_database = src.globals.mydb.command("count", "people")
        return total_in_database


def type_of_search_selection():
    while True:
        clear()
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-       P/p(Identity Register)              -\n"
                                       f"+       V/v(Vehicle Register)               +\n"
                                       f"-                                           -\n"
                                       f"+          [ E/e(Exit) ]                    +\n"
                                       f"-                                           -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True, colour="blue")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("p"):
            # Search ID
            searches.search()

        elif usr_sel.__contains__("v"):
            # Vehicle search
            searches.vehicle_search()

        elif usr_sel.lower().strip(" ") == "e":
            break
        else:
            pass


def type_of_generating():
    while True:
        clear()
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-              P/p(Identity Gen)            -\n"
                                       f"+              V/v(Vehicle Gen)             +\n"
                                       f"-                                           -\n"
                                       f"+               [ E/e(Exit) ]               +\n"
                                       f"-                                           -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True, colour="blue")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("p"):
            # ID Gen
            generate_people()

        elif usr_sel.__contains__("v"):
            # Vehicle gen
            generate_vehicle()

        elif usr_sel.lower().strip(" ") == "e":
            break
        else:
            pass


def main():
    global dbCurs
    clear()
    while True:
        clear()
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-       G/g(Generate Data) - (Admin)        -\n"
                                       f"+       S/s(Search) - (General)             +\n"
                                       f"-       SIM/sim(Simulation) - (DB_Heavy)    -\n"
                                       f"+                                           +\n"
                                       f"-                                           -\n"
                                       f"+          [ E/e(Exit) ]                    +\n"
                                       f"-                                           -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"In register:{get_statistics(1)}", instant=True, colour="yellow")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("g"):
            # Generate
            type_of_generating()

        elif usr_sel.__contains__("sim"):
            # List
            realism_simulation()
            enter_to_continue()

        elif usr_sel.__contains__("s"):
            type_of_search_selection()

        elif usr_sel.__contains__("e"):
            # Exit
            print("Exiting...")
            file = open(glob.settings_file_location, "a+")
            file.write(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                       f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] (EXITING...)\n"
                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
            file.close()
            exit(0)





def generate_log_dir_files():
    file = open(glob.settings_file_location, "a+")
    file.write(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
               f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] (INITIALIZING)\n"
               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    file.close()


if __name__ == '__main__':
    change_windowSize()
    generate_log_dir_files()
    main()
