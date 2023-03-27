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
