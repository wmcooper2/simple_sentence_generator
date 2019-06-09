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
                       TAG_LIST,
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


def word_combos(tagged: List[Tuple[Text, Text]]) -> List[List[Text]]:
    """Creates a list of lists of vocab words. Returns List of Lists."""
#     tags = [word[1] for word in tagged]
    tags = pos_tags(tagged)
#     return [load_file(tag) for tag in tags if tag in TAG_LIST else tag[1]]
    return [load_file(tag) if tag in TAG_LIST else tag for tag in tags]


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

    pprint(word_combos(tagged))

    # load all the words from the pos_tag files as a list of lists
    #       The total amount of words is low so this is okay for now.




# for each pos tag in the sent
#   load the appropriate pos tag file
#   store the returned list as a value in a dict with key=pos_tag
#   
# 
# 
# 
# 
# 
# 


    # load specific vocab for a pos_tag identifier

# make random sentences by only using the given sentence pattern and vocab

if __name__ == "__main__":
    sentences = list(enumerate(load_file(SENTENCE_FILE), start=1))
    vocabulary = load_file(VOCABULARY_FILE)
    main(vocabulary, sentences)
