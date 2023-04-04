import datetime
import json
import os.path

import src_files.headers as head
import src_files.globals as glob

currencies = ['United States Dollar (USD)', 'Euro (EUR)', 'Japanese Yen (JPY)', 'British Pound (GBP)',
              'Swiss Franc (CHF)', 'Canadian Dollar (CAD)', 'Australian Dollar (AUD)', 'New Zealand Dollar (NZD)',
              'Chinese Yuan Renminbi (CNY)', 'Hong Kong Dollar (HKD)', 'Singapore Dollar (SGD)',
              'South Korean Won (KRW)', 'Indian Rupee (INR)', 'Brazilian Real (BRL)', 'Russian Ruble (RUB)',
              'South African Rand (ZAR)']


def log_transaction(sender, reciever, amount, successful: bool = True):
    if successful:
        dyn_text = f"[TRANSACTION SUCCESSFUL] [{sender['account_ownership']}]({sender['account_identification']}) >- [{amount} {head.random.choice(currencies)}] -> [{reciever['account_ownership']}]({reciever['account_identification']})"
        head.styled_coloured_print_centered(
            text=dyn_text,
            instant=True, colour="green")
    else:
        dyn_text = f"[TRANSACTION FAILED] {sender['account_ownership']}'s account ({sender['account_identification']}) has insufficient balance to transfer {amount} {head.random.choice(currencies)}."
        head.styled_coloured_print_centered(
            text=dyn_text,
            instant=True, colour="orange")
    head.write_to_file(text_to_write=f"[{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}] {dyn_text}\n",
                       typeOfWrite="a", path_to_file=glob.settings_file_location)


def log_reason_for_search(prepared):
    # Prevent the use of unnecessary searches without a specified reason.
    head.styled_coloured_print_centered(text="""
    ####################################################################################
    #       To make a search in the database you will have to provide a reason.        #
    #       This is to prevent unnecessary and non-legitimate searches to be made.     #
    ####################################################################################
    """, instant=True, colour="orange")
    head.styled_coloured_print_centered(text=f"\n\nReason for search: ", instant=True, colour="blue")
    while True:
        reason = head.styled_input(" >> ")
        if head.is_ascii(reason):
            # Valid input
            try:
                if prepared:
                    return reason
                else:
                    admin_usage_log(output_file="PDBSearchLog", content=reason, type="DATABASE_SEARCH")
            except Exception as e:
                print(e)
            break
        else:
            # Invalid input
            head.styled_coloured_print_centered(text="Invalid input, please try again.", colour="red", instant=True)


def admin_usage_log(output_file: str, content, type: str, prepared: bool = False, prep_msg=None):
    if not prepared:
        try:
            if not os.path.exists(f"./ADMIN"):
                os.mkdir("./ADMIN")
                os.system("attrib +h " + "./ADMIN")
            with open(f"./ADMIN/{output_file}.log", "w") as f:
                if type == "DATABASE_SEARCH":
                    f.write(f"###############| {datetime.datetime.now()} |###############\n"
                            f"Type: DATABASE_SEARCH\n"
                            f"Reason: {content}\n"
                            f"###########################################################\n")
                else:
                    f.write(f"###############| {datetime.datetime.now()} |###############\n"
                            f"Content: {content}\n"
                            f"###########################################################\n")
        except Exception as e:
            print(e)
    else:
        if prep_msg is not None:
            try:
                if not os.path.exists(f"./.ADMIN"):
                    os.mkdir("./ADMIN")
                    os.system("attrib +h " + "./ADMIN")
                with open(f"./ADMIN/{output_file}.log", "w") as f:
                    if type == "DATABASE_SEARCH":
                        f.write(f"###############| {datetime.datetime.now()} |###############\n"
                                f"TYPE: DATABASE_SEARCH\n"
                                f"REASON: {content}\n"
                                f"SEARCH:{prep_msg[0]}\n"
                                f"WHERE: {prep_msg[1]}\n"
                                f"###########################################################\n")
                    else:
                        f.write(f"###############| {datetime.datetime.now()} |###############\n"
                                f"Content: {content}\n"
                                f"###########################################################\n")
            except Exception as e:
                print(e)


def log_db_search_to_file(all_results):
    try:
        if not os.path.exists("./db_search"):
            os.mkdir("./db_search")
        with open("./db_search/db_search.txt", "w") as f:
            f.write("----------------------------------------------------------------\n")
            f.write("BEFORE\n")
            for i in all_results:
                f.write(f"[Government Name]: {i.get('first_name')} {i.get('last_name')}\n"
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
            f.write("AFTER\n")
    except Exception as e:
        print(e)
