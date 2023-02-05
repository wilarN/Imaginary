import src.searches

from src.headers import *


def change_windowSize():
    cmd = "mode con: cols=200 lines=50"
    os.system(cmd)

def list_people():
    # List all people
    for document in dbCurs:
        print(
            f"{document.get('first_name')} {document.get('last_name')}, {document.get('age')} y/o, {document.get('height')}cm, {document.get('nationality')}.")


def get_statistics(selection: int):
    if selection == 1:
        total_in_database = mydb.command("count", "people")
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
                                       f"-       L/l(List Register) - (DB_Heavy)     -\n"
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

        elif usr_sel.__contains__("l"):
            # List
            list_people()
            enter_to_continue()

        elif usr_sel.__contains__("s"):
            type_of_search_selection()

        elif usr_sel.__contains__("e"):
            # Exit
            print("Exiting...")
            del dbCurs
            exit(0)


if __name__ == '__main__':
    change_windowSize()
    main()
