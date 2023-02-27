import markovify
from time import sleep
import json
import os

# Open the JSON file and extract the "body" field from each comment
messages = []


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


def simulate_comms():
    text = pre_init()
    from src_files.simulation import stop_event, head, glob, random, log_transaction
    # Build the Markov chain model
    text_model = markovify.Text(text)
    print("Starting simulation...")
    while not stop_event.is_set():
        print("Generating sentence...")
        sleep(head.random.uniform(0, 1))

        # Generate 5 random sentences
        text = str(''.join(text))
        for i in range(5):
            sentence = text_model.make_short_sentence(min_chars=20, max_chars=30)
            print(sentence)