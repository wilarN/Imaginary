import re

from headers import *


def search():
    global mycol
    mycol = mydb["people"]
    global dbCurs
    clear()
    styled_coloured_print_centered(text="""
    ##############################################################################
    # We trust you have received the usual lecture from the                      #
    # Administrator or Organisation. It usually boils down to these four things: #
    #                                                                            #
    # #1) Respect the privacy of others.                                         #
    # #2) Think before you type/search.                                          #
    # #3) Reason for your lookup.                                                #
    # #4) With great power comes great responsibility.                           #
    #                                                                            #
    ##############################################################################
    """, instant=True, colour="yellow")
    enter_to_continue()

    while True:
        clear()
        tab_down()
        styled_coloured_print_centered(text=f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                            f"-  |   Identity Search  | -\n"
                                            f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                            f"-    [1]- First Name      -\n"
                                            f"+    [2]- Last Name       +\n"
                                            f"-    [3]- P'IdentNum      -\n"
                                            f"+    [4]- Eye Colour      +\n"
                                            f"-    [5]- Height          -\n"
                                            f"+    [6]- Nationality     +\n"
                                            f"-                         -\n"
                                            f"+                         +\n"
                                            f"-      [ E/e(Exit) ]      -\n"
                                            f"+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True, colour="blue")
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
                f"{i.get('first_name')} {i.get('last_name')}, {i.get('sex')}, {i.get('age')} y/o, {i.get('height')}cm, {i.get('nationality')}, ({i.get('personal_identification_number')})")
            line()
        enter_to_continue()


def vehicle_search():
    mycol = mydb["vehicles"]
    global dbCurs
    clear()
    styled_coloured_print_centered(text="""
    ##############################################################################
    # We trust you have received the usual lecture from the                      #
    # Administrator or Organisation. It usually boils down to these four things: #
    #                                                                            #
    # #1) Respect the privacy of others.                                         #
    # #2) Think before you type/search.                                          #
    # #3) Reason for your lookup.                                                #
    # #4) With great power comes great responsibility.                           #
    #                                                                            #
    ##############################################################################
    """, instant=True, colour="yellow")
    enter_to_continue()

    while True:
        clear()
        tab_down()
        styled_coloured_print_centered(text=f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                            f"-  |   Vehicle Lookup  |  -\n"
                                            f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                            f"-    [1]- Model           -\n"
                                            f"+    [2]- Manufacturer    +\n"
                                            f"-    [3]- Colour          -\n"
                                            f"+    [4]- Year            +\n"
                                            f"-    [5]- Annotations     -\n"
                                            f"+    [6]- Car-Body Type   +\n"
                                            f"-    [7]- Plate Number    -\n"
                                            f"+                         +\n"
                                            f"-                         -\n"
                                            f"+                         +\n"
                                            f"-      [ E/e(Exit) ]      -\n"
                                            f"+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True, colour="blue")
        tab_down()
        usr_sel = input(" >> ")
        if usr_sel.lower().strip(" ") == "e":
            break
        elif usr_sel.lower().strip(" ") == "1":
            # Model Search
            usr_sel = input(" Model >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'model': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "2":
            # Manufacturer search
            usr_sel = input(" Manufacturer >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'manufacturer': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "3":
            # Colour search
            usr_sel = input(" Colour >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'colour': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "4":
            # Year Search
            usr_sel = input(" Year >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'year': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "5":
            # annotations Search
            usr_sel = input(" Annotations >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'annotations': re.compile(r".*" + f"{usr_sel}" + r".*")
                })

                dbCurs = mycol.find(
                    filter=filter
                )

        elif usr_sel.lower().strip(" ") == "6":
            # Car_body search
            usr_sel = input(" Car-body (ex. 'Sedan' 'Coupe') >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = ({
                    'car_body': re.compile(r".*" + f"{usr_sel}" + r".*")
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
                f"{i.get('model')} {i.get('manufacturer')}, {i.get('colour')}, {i.get('year')}, {i.get('annotations')}, {i.get('car_body')}, ({i.get('plate')})")
            line()
        enter_to_continue()
