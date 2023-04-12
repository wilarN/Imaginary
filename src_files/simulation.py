import src_files.headers as head
import threading
import src_files.globals as glob
import random
from src_files.logging import *
from src_files.virt_messages import simulate_comms
from time import sleep


def money_transaction():
    # Transaction logic.
    while not stop_event.is_set():
        sleep(head.random.uniform(0, 1))
        # Get two random customers from the database
        customers = glob.mycol.aggregate([{"$sample": {"size": 2}}])

        customer_list = list(customers)
        sender = customer_list[0]
        receiver = customer_list[1]

        sender_account = random.choice(sender["bank_accounts"])
        # amount = 100  # Change this to the desired transaction amount
        amount = head.random.randint(100, 100000)

        receiver_account = random.choice(receiver["bank_accounts"])

        if sender_account["balance"] >= amount:
            glob.mycol.update_one({"_id": sender["_id"]},
                                  {"$inc": {"bank_accounts.$[elem].balance": -amount}},
                                  array_filters=[
                                      {"elem.account_identification": sender_account["account_identification"]}])
            glob.mycol.update_one({"_id": receiver["_id"]},
                                  {"$inc": {"bank_accounts.$[elem].balance": amount}}, array_filters=[
                    {"elem.account_identification": receiver_account["account_identification"]}])
            # head.styled_coloured_print_centered(text=f"\n[TRANSACTION SUCCESSFUL] [[{sender_account['account_ownership']}]({sender_account['account_identification']}) >- [{amount} {head.random.random.choice(currencies)}] -> [{receiver_account['account_ownership']}]({receiver_account['account_identification']})]", instant=True, colour="green")
            log_transaction(successful=True, sender=sender_account, reciever=receiver_account, amount=amount)
        else:
            # head.styled_coloured_print_centered(text=f"\n[TRANSACTION FAILED] {sender_account['account_ownership']}'s account ({sender_account['account_identification']}) has insufficient balance to transfer {amount}", instant=True, colour="orange")
            log_transaction(successful=False, sender=sender_account, reciever=receiver_account, amount=amount)


def relaionship_scrambler():
    """
    Scrambles the relationships between the people in the database.
    """
    genders = ["Male", "Female"]

    while not stop_event.is_set():
        # Assuming the relationship status is stored as a field called "relationship_status"

        # Create a list of genders to randomly select from
        genders = ["Male", "Female"]

        # Select one random gender from the list
        selected_gender = random.choice(genders)

        # Build the query using the selected gender and relationship status
        query = [
            {"$match": {"gender": selected_gender, "relationship_status": "Single"}},
            {"$sample": {"size": 1}}
        ]

        # Select one random person matching the selected gender and relationship status
        random_person = list(glob.mycol.aggregate(query))[0]

        glob.mycol.update_one({"_id": random_person["_id"]}, {"$set": {"relationship_status": "Married"}})
        # Remove the selected gender from the list
        genders.remove(selected_gender)

        # Select one random person from the remaining gender and relationship status
        query = [
            {"$match": {"gender": genders[0], "relationship_status": "Single"}},
            {"$sample": {"size": 1}}
        ]
        random_person_2 = list(glob.mycol.aggregate(query))[0]

        glob.mycol.update_one({"_id": random_person["_id"]}, {"$set": {"relationship_status": "Married"}})

        # Combine the two random people into a list
        random_people = [random_person, random_person_2]
        head.styled_coloured_print_centered(text=f"{random_person['first_name']} {random_person['last_name']} married {random_person_2['first_name']} {random_person_2['last_name']}.")


def crime_activity():
    # Crime logic.
    while not stop_event.is_set():
        pass


stop_event = threading.Event()


def realism_simulation():
    head.styled_coloured_print_centered(text="""
    ##############################################################################
    # All of the following simulations will affect and modify the stored data    #
    # including database records of identities and ownerships of cars etc.       #
    # Please proceed with caution.                                               #
    ##############################################################################
    """, instant=True, colour="yellow")
    head.enter_to_continue()
    while True:
        head.clear()
        head.styled_coloured_print_centered(text=

                                                   f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                                   f"-           [1]- Phone Simulation           -\n"
                                                   f"+           [2]- Bank Simulation            +\n"
                                                   f"-                                           -\n"
                                                   f"+                                           +\n"
                                                   f"-                                           -\n"
                                                   f"+               [ E/e(Exit) ]               +\n"
                                                   f"-                                           -\n"
                                                   f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n", instant=True)

        head.tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("1"):
            head.tab_down()

            head.styled_coloured_print_centered(text="Simulation of phone-message person to person communication started... ", instant=True)

            sleep(1)
            print()
            head.styled_coloured_print_centered(text="To stop the simulation do not use ctrl-c, please press `ENTER` to gracefully stop.", instant=True)
            sleep(1)
            # Create a thread for the virtual messaging
            simulate_comms_thread = threading.Thread(target=simulate_comms)
            simulate_comms_thread.start()

            while True:
                head.enter_to_continue()
                break
            # Stop the thread here
            stop_event.set()
            simulate_comms_thread.join()
            stop_event.clear()
            break

        elif usr_sel.__contains__("2"):
            head.tab_down()
            head.styled_coloured_print_centered(text="Full simulation of activities and logic started... ")
            sleep(1)
            print()
            head.styled_coloured_print_centered(
                text="To stop the simulation do not use ctrl-c, please press `ENTER` to gracefully stop.", instant=True)
            sleep(5)

            # Full simulation --> Transactions, crime, car trade, property etc.
            # Create a thread for the money transaction
            money_transaction_thread = threading.Thread(target=money_transaction)
            money_transaction_thread.start()

            while True:
                head.enter_to_continue()
                break
            # Stop the thread here
            stop_event.set()
            money_transaction_thread.join()
            stop_event.clear()
            break
        elif usr_sel.__contains__("3"):
            head.tab_down()
            head.styled_coloured_print_centered(text="Scrambling the relationship statuses of people in the database.")
            sleep(1)
            print()
            head.styled_coloured_print_centered(
                text="To stop the simulation do not use ctrl-c, please press `ENTER` to gracefully stop.", instant=True)
            sleep(5)
            scramble_rel_thread = threading.Thread(target=relaionship_scrambler)
            scramble_rel_thread.start()

            while True:
                head.enter_to_continue()
                break
            # Stop the thread here
            stop_event.set()
            scramble_rel_thread.join()
            stop_event.clear()
            break

        elif usr_sel.__contains__("e"):
            break
