"""sentencegen.py; generate sentences based on given sentence structure and a given vocabulary."""
# stand lib
from pathlib import Path
from pprint import pprint
import random
from typing import Any
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
                       PUNCTUATION,
                       SENTENCE_FILE,
                       TAG_LIST,
                       VOCABULARY_FILE,
                       WELCOME_MESSAGE,)


def all_elements_are_list_type(list_: List[List[Text]]) -> bool:
    """Check that all elements of 'list_' are lists. Returns Boolean."""
    return all(is_list_type(el) for el in list_)


def all_possibilities(string: Text, 
                      words: List[List[Text]], 
                      all_: List[Text]) -> List[Text]:
    """Recursively get all combinations of 'words' lists without
       changing the order of the lists. Returns List."""
    for word in words[0]:
        sent_so_far = " ".join([string, word])
        try:
            recfun(sent_so_far, words[1:])
        except IndexError:
            all_.append(sent_so_far.strip())


def change_word(word: Text, choices: List[Text]) -> Text:
    """Choose a word from 'choices' different from 'word'. Returns String."""
    choices.remove(word)
    return random.choice(choices)


def get_sent_choice(choice: int, sentences: List[Text]) -> Text:
    """Gets the chosen sentence. Returns String."""
    return sentences[choice - 1][1]


def is_list_type(arg: Any) -> bool:
    """Checks if 'arg' is of list type. Returns Boolean."""
    return isinstance(arg, list)


def load_file(file_: Text) -> List[Text]:
    """Loads a 'file. Returns List."""
    try:
        temp = []
        with open(file_, "r") as f:
            for line in f.readlines():
                temp.append(line.strip())
        return temp
    except FileNotFoundError:
        return []


def pos_tag_word_list(tagged: List[Tuple[Text, Text]]) -> List[List[Text]]:
    """Creates a list of lists of vocab words. Returns List of Lists."""
    tags = pos_tags(tagged)
    return [load_file("tagdata/" + tag + ".txt") if tag in TAG_LIST else tag for tag in tags]


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
    
    #TESTING
#     pprint(tagged)
    pprint(pos_tag_word_list(tagged))
#     pprint(remove_simple_punctuation_tags(pos_tag_word_list(tagged)))
#     temp = remove_simple_punctuation_tags(pos_tag_word_list(tagged))
#     pprint(remove_word_tags(temp))

    # TODO:
        # confirm that all elements are list elements (for uniformity)
        # load specific vocab for a pos_tag identifier
        # calculate how many sentences possible
        # save all the sentence possibilities to a text file
        # 







def remove_simple_punctuation_tags(list_: List[Text]) -> List[Text]:
    """Removes the punctuation tags from 'list_'. Returns List"""
    return [item for item in list_ if item not in PUNCTUATION]

def remove_word_tags(list_: List[Text]) -> List[Text]:
    """Removes the word tags from 'list_'. Returns List"""
    return [item for item in list_ if item not in TAG_LIST]


if __name__ == "__main__":
    sentences = list(enumerate(load_file(SENTENCE_FILE), start=1))
    vocabulary = load_file(VOCABULARY_FILE)
    main(vocabulary, sentences)
