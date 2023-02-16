from src.headers import *
import threading
import src.globals as glob
from random import choice
def money_transaction():
    # Transaction logic.
    while not stop_event.is_set():
        time.sleep(1)
        print("TEST.")
        # Get two random customers from the database
        customers = glob.mycol.aggregate([{"$sample": {"size": 2}}])

        # Perform transaction between the two customers
        for customer in customers:
            account = src.headers.random.choice(customer["bank_accounts"])
            amount = 100  # Change this to the desired transaction amount
            # Find the other customer's bank account and perform transaction
            other_customer = glob.mycol.find_one({"_id": {"$ne": customer["_id"]}})
            other_account = src.headers.random.choice(other_customer["bank_accounts"])
            if account["balance"] >= amount:
                glob.mycol.update_one({"_id": customer["_id"]},
                                             {"$inc": {"bank_accounts.$[elem].balance": -amount}},
                                             array_filters=[
                                                 {"elem.account_identification": account["account_identification"]}])
                glob.mycol.update_one({"_id": other_customer["_id"]},
                                             {"$inc": {"bank_accounts.$[elem].balance": amount}}, array_filters=[
                        {"elem.account_identification": other_account["account_identification"]}])
                print(
                    f"Transferred {amount} from {account['account_ownership']}'s account ({account['account_identification']}) to {other_account['account_ownership']}'s account ({other_account['account_identification']})")
            else:
                print(
                    f"{account['account_ownership']}'s account ({account['account_identification']}) has insufficient balance to transfer {amount}")


def crime_activity():
    # Crime logic.
    while not stop_event.is_set():
        pass


stop_event = threading.Event()


def realism_simulation():
    src.headers.styled_coloured_print_centered(text="""
    ##############################################################################
    # All of the following simulations will affect and modify the stored data    #                      #
    # including database records of identities and ownerships of cars etc.       #
    # Please proceed with caution.                                               #
    ##############################################################################
    """, instant=True, colour="yellow")
    src.headers.enter_to_continue()
    while True:
        src.headers.clear()
        src.headers.styled_coloured_print_centered(text=
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n"
                                       f"-       [1]- Crime Simulation               -\n"
                                       f"+       [2]- Full Simulation                +\n"
                                       f"-                                           -\n"
                                       f"+                                           +\n"
                                       f"-                                           -\n"
                                       f"+          [ E/e(Exit) ]                    +\n"
                                       f"-                                           -\n"
                                       f"+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n", instant=True)
        src.headers.tab_down()
        usr_sel = input(" >> ")
        usr_sel = usr_sel.lower().strip(" ")
        if usr_sel.__contains__("1"):
            pass
        if usr_sel.__contains__("2"):
            # Full simulation --> Transactions, crime, car trade, property etc.
            # Create a thread for the money transaction
            money_transaction_thread = threading.Thread(target=money_transaction)
            money_transaction_thread.start()

            while True:
                src.headers.tab_down()
                src.headers.styled_coloured_print_centered(text="Full simulation of activities and logic started... "
                                                                "Press enter to cancel.")
                src.headers.enter_to_continue()
                break
            # Stop the thread here
            stop_event.set()
            money_transaction_thread.join()
            break

        elif usr_sel.__contains__("e"):
            break
