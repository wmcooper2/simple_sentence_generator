"""sentencegen.py; generate sentences based on given sentence structure and a given vocabulary."""
# stand lib
from pathlib import Path
from pprint import pprint
import random
from typing import Text
from typing import Tuple
from typing import List

# 3rd party
from tabulate import tabulate
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# custom
from constants import (CHOICE_MESSAGE,
                       NOT_A_NUMBER_ERROR,
                       SENTENCE_FILE,
                       VOCABULARY_FILE,
                       WELCOME_MESSAGE,)


def change_word(word: Text, choices: List[Text]) -> Text:
    """Choose a word from 'choices' different from 'word'. Returns String."""
    choices.remove(word)
    return random.choice(choices)


def get_sent_choice(choice: int, sentences: List[Text]) -> Text:
    """Gets the chosen sentence. Returns String."""
    return sentences[choice - 1][1]


def load_file(file_: Text) -> List[Text]:
    """Loads a text file. Returns List."""
    try:
        temp = []
        with open(file_, "r") as f:
            for line in f.readlines():
                temp.append(line.strip())
        return temp
    except FileNotFoundError:
        return []





def pos_tags(tokens: List[Tuple[Text, Text]]) -> List[Text]:
    """Get the pos tags of 'tokens'. Returns List."""
    return [tag[1] for tag in tokens]


def main(vocab: List[Tuple[Text, Text]], sents: List[Text]) -> None:

    # Display sentences
    answer = input(WELCOME_MESSAGE)
    print(tabulate(sents))

    # User chooses one with a number
    choice = -1
    while choice not in range(1, len(sentences) + 1):
        try:
            choice = int(input(CHOICE_MESSAGE))
        except ValueError:
            print(NOT_A_NUMBER_ERROR)
    sentence_choice = get_sent_choice(choice, sents)
    tokens = word_tokenize(sentence_choice)
    tagged = pos_tag(tokens)

# load vocabulary
    # make list of the parts of speech of the vocabulary
# make random sentences by only using the given sentence pattern and vocab

    # When User makes a choice, program asks for an amount.
        # if the user makes a mistake, then the options are presented again
    # Program makes a text file with the amount of sentences requested.

if __name__ == "__main__":
    sentences = list(enumerate(load_file(SENTENCE_FILE), start=1))
    vocabulary = load_file(VOCABULARY_FILE)
    main(vocabulary, sentences)
