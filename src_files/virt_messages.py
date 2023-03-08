import markovify
from time import sleep
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
    file = open("src_files/data/text_data/WizardsOfEldoria.txt", 'r', errors='ignore')
    text = file.read()
    file.close()
    return text


def simulate_comms():
    # text = pre_init()
    text = messages
    from src_files.simulation import stop_event, head, glob, random, log_transaction
    # Build the Markov chain model
    text_model = markovify.Text(text)

    while not stop_event.is_set():
        sleep(head.random.uniform(0, 1))

        # Generate 5 random sentences
        for i in range(5):
            sentence = text_model.make_short_sentence(min_chars=20, max_chars=30)
            print(sentence)