import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import gutenberg
from collections import defaultdict
import random

nltk.download('gutenberg')
corpus = gutenberg.raw('shakespeare-hamlet.txt')

def train_markov_chain(corpus):
    # Tokenize the corpus
    tokens = word_tokenize(corpus)

    # Create a dictionary to store the Markov chain
    chain = defaultdict(list)

    # Populate the Markov chain dictionary
    for i in range(len(tokens) - 2):
        chain[(tokens[i], tokens[i+1])].append(tokens[i+2])

    return chain

def generate_text(chain, length=100):
    # Choose a random starting word pair
    current = random.choice(list(chain.keys()))

    # Generate text using the Markov chain
    result = list(current)
    for i in range(length):
        next_word = random.choice(chain[current])
        result.append(next_word)
        current = (current[1], next_word)

    return ' '.join(result)

