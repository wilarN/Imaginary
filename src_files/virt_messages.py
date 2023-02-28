import markovify
from time import sleep
import json

# Creates some issues
from convokit import Corpus, download
import os

# Open the JSON file and extract the "body" field from each comment
messages = []


# temp doesnt work.
corpus = Corpus(filename=download("reddit-corpus-small"))


def pre_init():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir_path}/data/text_data/RC_2008-09') as f:
        batch_size = 500
        while True:
            lines = f.readlines(batch_size)
            if not lines:
                break
            for line in lines:
                comment = json.loads(line)
                if 'body' in comment:
                    messages.append(comment['body'])

    # Print the first 10 messages
    # print(messages[:10])
    return messages


def pre_init_story():
    # Load the input text file for the "model" or whatever.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = open(f"{dir_path}/data/text_data/WizardsOfEldoria.txt", 'r', errors='ignore')
    text = file.read()
    file.close()
    return text


def simulate_comms():
    # text = pre_init()
    text = pre_init_story()
    from src_files.simulation import stop_event, head, glob, log_message_communication
    # Build the Markov chain model
    text_model = markovify.Text(text)
    # print("Starting simulation...")
    while not stop_event.is_set():
        # print("Generating sentence...")
        sleep(head.random.uniform(0.5, 4))

        # Generate 5 random sentences
        text = str(''.join(text))
        sentence = text_model.make_short_sentence(max_chars=50)

        # Creates issues
        # sentence = corpus.random_utterance()
        sentence = sentence.text
        if sentence:
            customers = glob.mycolPhone.aggregate([{"$sample": {"size": 2}}])

            customer_list = list(customers)
            sender = customer_list[0]
            receiver = customer_list[1]

            log_message_communication(message=sentence, sender=sender, successful=True, reciever=receiver)
