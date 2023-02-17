import markovify

# Load the input text file
with open("./data/text_data/WizardsOfEldoria.txt", 'r', errors='ignore') as f:
    text = f.read()

# Build the Markov chain model
text_model = markovify.Text(text)

# Generate 5 random sentences
for i in range(5):
    sentence = text_model.make_sentence()
    print(sentence)