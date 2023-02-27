import markovify
from time import sleep


def pre_init():
    # Load the input text file for the "model" or whatever.
    file = open("src/data/text_data/WizardsOfEldoria.txt", 'r', errors='ignore')
    text = file.read()
    file.close()
    return text


def simulate_comms():
    text = pre_init()
    from simulation import stop_event, head, glob, choice, log_transaction
    # Build the Markov chain model
    text_model = markovify.Text(text)

    while not stop_event.is_set():
        sleep(head.random.uniform(0, 1))


        # Get two random customers from the database
        customers = glob.mycol.aggregate([{"$sample": {"size": 2}}])

        # Perform transaction between the two customers
        customer_list = list(customers)
        sender = customer_list[0]
        receiver = customer_list[1]

        sender_account = choice(sender["bank_accounts"])
        # amount = 100  # Change this to the desired transaction amount
        amount = head.random.randint(100, 100000)

        receiver_account = choice(receiver["bank_accounts"])

        if sender_account["balance"] >= amount:
            glob.mycol.update_one({"_id": sender["_id"]},
                                  {"$inc": {"bank_accounts.$[elem].balance": -amount}},
                                  array_filters=[
                                      {"elem.account_identification": sender_account["account_identification"]}])
            glob.mycol.update_one({"_id": receiver["_id"]},
                                  {"$inc": {"bank_accounts.$[elem].balance": amount}}, array_filters=[
                    {"elem.account_identification": receiver_account["account_identification"]}])
            # head.styled_coloured_print_centered(text=f"\n[TRANSACTION SUCCESSFUL] [[{sender_account['account_ownership']}]({sender_account['account_identification']}) >- [{amount} {head.random.choice(currencies)}] -> [{receiver_account['account_ownership']}]({receiver_account['account_identification']})]", instant=True, colour="green")
            log_transaction(successful=True, sender=sender_account, reciever=receiver_account, amount=amount)
        else:
            # head.styled_coloured_print_centered(text=f"\n[TRANSACTION FAILED] {sender_account['account_ownership']}'s account ({sender_account['account_identification']}) has insufficient balance to transfer {amount}", instant=True, colour="orange")
            log_transaction(successful=False, sender=sender_account, reciever=receiver_account, amount=amount)











        # Generate 5 random sentences
        for i in range(5):
            sentence = text_model.make_sentence()
            print(sentence)