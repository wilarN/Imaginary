

# from headers import *
# import globals as glob
import src_files.generate, src_files.simulation
from src_files.headers import *
import src_files.globals as glob
from src_files.logging import log_db_search_to_file, log_reason_for_search, admin_usage_log


def get_formatted_list(items):
    for item in items:
        print(f"[{item}], ", end="")


def search():
    global mycol
    mycol = glob.mydb["people"]
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
    clear()

    while True:
        clear()
        tab_down()

        reason = log_reason_for_search(prepared=True)
        if not reason:
            break
            
        styled_coloured_print_centered(text=f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                            f"-  |   Identity Search  | -\n"
                                            f"+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                            f"-    [1]- First Name      -\n"
                                            f"+    [2]- Last Name       +\n"
                                            f"-    [3]- P'IdentNum      -\n"
                                            f"+    [4]- Eye Colour      +\n"
                                            f"-    [5]- Height          -\n"
                                            f"+    [6]- Nationality     +\n"
                                            f"-    [7]- Records &       -\n"
                                            f"+       & Annotations     +\n"
                                            f"-                         -\n"
                                            f"+                         +\n"
                                            f"-                         -\n"
                                            f"+                         +\n"
                                            f"-                         -\n"
                                            f"+                         +\n"
                                            
                                            f"-      [ E/e(Exit) ]      -\n"
                                            f"+-+-+-+-+-+-+-+-+-+-+-+-+-+", instant=True, colour="blue")
        tab_down()
        usr_sel = input(" >> ")
        type_of_search = None

        if usr_sel.lower().strip(" ") == "e":
            break
        elif usr_sel.lower().strip(" ") == "1":
            # First_name Search
            type_of_search = "FNAME"
            usr_sel = input(" Name >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'first_name': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "2":
            # Last_name search
            type_of_search = "LNAME"
            usr_sel = input(" Surname >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'last_name': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "3":
            # Personal Identification Number search
            type_of_search = "PIDN(PersonalIDNum)"
            usr_sel = input(" Personal Identification Number (ex. 19990101-9984) >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'personal_identification_number': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "4":
            # Eye Colour Search
            type_of_search = "EYECOL"
            usr_sel = input(" Eye Colour >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'eye_colour': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "5":
            # Height Search
            type_of_search = "HEIGHT"
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
            type_of_search = "NATIONALITY"
            usr_sel = input(" Nationality >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'nationality': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)
        elif usr_sel.lower().strip(" ") == "7":
            # Annotations and record search
            type_of_search = "ANNOTATIONRECORD"
            print(ANNOTATIONS_AND_CRIMES)
            usr_sel = input(" Crime // Annotation >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'record_and_annotations': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        else:
            break

        admin_usage_log(output_file="PDBSearchLog", content=reason,
                        type="DATABASE_SEARCH", prepared=True, prep_msg=[usr_sel, str(type_of_search)])

        tab_down()
        line()

        if not os.path.exists("./db_search"):
            os.mkdir("./db_search")

        with open("./db_search/db_search.txt", "w") as f:
            f.write("----------------------------------------------------------------\n")

            for i in dbCurs:
                styled_coloured_print_centered(text=f"""
    FOUND IN DNA DATABASE: {match_dna(i.get('dna_sequence'))}\n
    [Government Name]: {i.get('first_name')} {i.get('last_name')}\n
      - [Gender]: {i.get('sex')}
      - [Age]: {i.get('age')} y/o
      - [Height]: {i.get('height')}cm
      - [Nationality]: {i.get('nationality')}
      - [Personal Identification Number]: ({i.get('personal_identification_number')})
      - [Records & Annotations]:
            {i.get('record_and_annotations')}
      - [Cars]:
            {i.get('cars')}
                    """, instant=True, colour="yellow", cent=False)
                f.write(f"FOUND IN DNA DATABASE: {match_dna(i.get('dna_sequence'))}\n"
                        f"[Government Name]: {i.get('first_name')} {i.get('last_name')}\n"
                        f"- [Gender]: {i.get('sex')}\n"
                        f"- [Age]: {i.get('age')} y/o\n"
                        f"- [Height]: {i.get('height')}cm\n"
                        f"- [Nationality]: {i.get('nationality')}\n"
                        f"- [Personal Identification Number]: ({i.get('personal_identification_number')})\n"
                        f"- [Records & Annotations]:\n"
                        f"{i.get('record_and_annotations')}\n"
                        f"- [Cars]:\n"
                        f"{i.get('cars')}\n"
                        "----------------------------------------------------------------\n")
                line()
        if yes_no("Open output file?"):
            try:
                open_file_in_editor("./db_search/db_search.txt")
            except Exception as e:
                print(e)
        enter_to_continue()


def vehicle_search():
    mycol = glob.mydb["vehicles"]
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
                                            f"+    [8]- Ownership(Name) +\n"
                                            f"-                         -\n"
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
                filter = {'model': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "2":
            # Manufacturer search
            usr_sel = input(" Manufacturer >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'manufacturer': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)
        elif usr_sel.lower().strip(" ") == "3":
            # Colour search
            usr_sel = input(" Colour >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'colour': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "4":
            # Year Search
            usr_sel = input(" Year >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'year': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "5":
            # annotations Search
            usr_sel = input(" Annotations >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'annotations': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "6":
            # Car_body search
            usr_sel = input(" Car-body (ex. 'Sedan' 'Coupe') >> ")
            usr_sel = usr_sel.strip(" ").capitalize()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'car_body': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "7":
            # Car_body search
            usr_sel = input("Plate (ex. XXX-99X) >> ")
            usr_sel = usr_sel.strip(" ").upper()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'plate': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        elif usr_sel.lower().strip(" ") == "8":
            # Car_body search
            usr_sel = input(" Registered Vehicle Owner (ex. 'John Doe' or 'John' or 'Doe') >> ")
            usr_sel = usr_sel.strip(" ").upper()
            if usr_sel.lower().strip(" ") == "e":
                break
            else:
                filter = {'owner': {'$regex': f".*{usr_sel}.*"}}
                dbCurs = mycol.find(filter=filter)

        else:
            break

        tab_down()
        line()
        for i in dbCurs:
            styled_coloured_print_centered(text=
                                           f"""[Owner]: {i.get('owner')}\n
  - [Model]: {i.get('model')}
  - [Manufacturer]: {i.get('manufacturer')}
  - [Colour]: {i.get('colour')}
  - [Body]: {i.get('car_body')}
  - [Production Year]: {i.get('year')}
  - [Annotations]: {i.get('annotations')}
  - [Plate]: {i.get('plate')}
""", instant=True, colour="yellow", cent=False)
            line()
        enter_to_continue()


def dna_search():
    """
    Searches the dna register for a match.
    """
    


