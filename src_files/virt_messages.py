import markovify
from time import sleep
from src_files.misc import names
from src_files.globals import mycol
import json
import os

# Open the JSON file and extract the "body" field from each comment
messages = []
# dir_path = os.path.dirname(os.path.realpath(__file__))
# with open(f'{dir_path}/data/text_data/RC_2008-09') as f:
#     for line in f:
#         comment = json.loads(line)
#         if 'body' in comment:
#             messages.append(comment['body'])
#
# # Print the first 10 messages
# print(messages[:10])


def pre_init():
    # Load the input text file for the "model" or whatever.
    file = open("src_files/data/text_data/Genz_convo.txt", 'r', errors='ignore')
    text = file.read()
    file.close()
    return text


def simulate_comms():
    people = mycol.aggregate([{"$sample": {"size": 2}}])
    customer_list = list(people)

    participants = []
    for i in [customer_list[0], customer_list[1]]:
        participants.append(i)

    text = pre_init()
    # text = messages
    from src_files.simulation import stop_event, head, glob, random, log_transaction
    # Build the Markov chain model
    text_model = markovify.Text(text)

    while not stop_event.is_set():
        prev_message = ""
        sleep(head.random.uniform(1, 3))
        sent = text_model.make_short_sentence(max_chars=50)
        if sent is not None:
            if sent != prev_message:
                prev_message = sent
                person = random.choice(participants)
                if len(person['phone_numbers']) < 1:
                    print(f"[ {person['first_name']} {person['last_name']}, [WEB-CLIENT] ]: {sent}")
                else:
                    print(f"[ {person['first_name']} {person['last_name']}, {person['phone_numbers']} ]: {sent}")
