from datetime import datetime

# GUI
import customtkinter
from PIL import Image
from src_files import searches, generate, simulation
from src_files.headers import *
import src_files.globals as glob

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
        total_in_database = src_files.globals.mydb.command("count", "people")
        return total_in_database


def type_of_search_selection():
    while True:
        clear()
        styled_coloured_print_centered(text=logo_ascii, colour="red", instant=True)
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-       P/p(Identity Register)              -\n"
                                       f"+       V/v(Vehicle Register)               +\n"
                                       f"-       D/d(DNA Database)                   -\n"
                                       f"+                                           +\n"
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

        elif usr_sel.__contains__("d"):
            # Search the DNA register.
            searches.dna_search()

        elif usr_sel.lower().strip(" ") == "e":
            break
        else:
            pass


def type_of_generating():
    while True:
        clear()
        styled_coloured_print_centered(text=logo_ascii, colour="red", instant=True)
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
            generate.generate_people()

        elif usr_sel.__contains__("v"):
            # Vehicle gen
            generate.generate_vehicle()

        elif usr_sel.lower().strip(" ") == "e":
            break
        else:
            pass


def drop_database():
    while True:
        clear()
        styled_coloured_print_centered(text=logo_ascii, colour="red", instant=True)
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-              [ DROP DATABASE ]            -\n"
                                       f"+   THIS ACTION IS UNREVERTABLE AND CANNOT  +\n"
                                       f"-   BE UNDONE. THIS WILL DROP ALL THE DATA  -\n"
                                       f"+   STORED IN THE DATABASE.                 +\n"
                                       f"-              PROCEED? (y/n)               -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True, colour="orange")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("y"):
            # DROP DB
            try:
                glob.myclient.drop_database("imaginaryMaster")
                clear()
                styled_coloured_print_centered(text=logo_ascii, colour="red", instant=True)
                styled_coloured_print_centered(text=
                                               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                               f"-                                           -\n"
                                               f"+    [ DATABASE DROPPED WITHOUT ERRORS ]    +\n"
                                               f"-                                           -\n"
                                               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True,
                                               colour="green")
            except Exception as e:
                clear()
                print(e)
                styled_coloured_print_centered(text=logo_ascii, colour="red", instant=True)
                styled_coloured_print_centered(text=
                                               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                               f"-                                           -\n"
                                               f"+        [ DATABASE DROPPED FAILED ]        +\n"
                                               f"-                                           -\n"
                                               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True,
                                               colour="red")
            tab_down()
            enter_to_continue()
            break
        elif usr_sel.__contains__("n"):
            # RETURN TO MENU
            break
        else:
            pass


def main():
    global dbCurs
    clear()
    while True:
        clear()
        styled_coloured_print_centered(text=logo_ascii, colour="red", instant=True)
        styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-       G/g(Generate Data) - (Admin)        -\n"
                                       f"+       S/s(Search) - (General)             +\n"
                                       f"-       SIM/sim(Simulation) - (DB_Heavy)    -\n"
                                       f"+       D/d(Drop Database) - (UNREVERTABLE) +\n"
                                       f"-                                           -\n"
                                       f"+          [ E/e(Exit) ]                    +\n"
                                       f"-                                           -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"In register:{get_statistics(1)}", instant=True, colour="yellow")
        tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("g"):
            # Generate Data // IDs - Vehicles
            type_of_generating()

        elif usr_sel.__contains__("sim"):
            # Simulate Events
            simulation.realism_simulation()
            enter_to_continue()

        elif usr_sel.__contains__("s"):
            # Search the database. // Interna Slagningar.
            type_of_search_selection()

        elif usr_sel.__contains__("d"):
            # Drop database // Delete all data.
            drop_database()

        elif usr_sel.__contains__("e"):
            # Exit // Quit
            glob.graceful_exit()


def generate_log_dir_files():
    file = open(glob.settings_file_location, "a+")
    file.write(f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
               f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] (INITIALIZING)\n"
               f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    file.close()


if __name__ == '__main__':
    generate_log_dir_files()

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    root = customtkinter.CTk()
    root.geometry("800x500")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Imaginary", width=100, height=80, font=("Roboto", 50))
    label.pack()

    generate_data_btn = customtkinter.CTkButton(master=frame, text="Generate Data", width=200, height=80,
                                                fg_color="black")
    generate_data_btn.pack(padx=20, pady=10)
    simulate_data = customtkinter.CTkButton(master=frame, text="Simulate", width=200, height=80, fg_color="black")
    simulate_data.pack(padx=20, pady=10)

    check = customtkinter.CTkCheckBox(master=frame, text="Master check")
    check.pack(padx=20, pady=20)

    root.mainloop()
    # main()
