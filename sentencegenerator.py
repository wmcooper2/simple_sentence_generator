"""sentencegen.py; generate sentences based on given sentence structure and a given vocabulary."""
# stand lib
from functools import reduce
import operator
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
from nltk.util import bigrams

# custom
from constants import (CHOICE_MESSAGE,
                       NOT_A_NUMBER_ERROR,
                       PUNCTUATION,
                       SENTENCE_FILE,
                       TAG_LIST,
                       VALID_BIGRAMS,
                       VOCABULARY_FILE,
                       WELCOME_MESSAGE,)


def all_elements_are_list_type(list_: List[List[Text]]) -> bool:
    """Check that all elements of 'list_' are lists. Returns Boolean."""
    return all(is_list_type(el) for el in list_)


sentence_combos = []
def all_possibilities(incomplete: Text,
                      words: List[List[Text]]) -> List[Text]:
    """Recursively get all combinations of 'words' lists without
       changing the order of the list elements. Returns List.

        -pass in a blank string ("") for the incomplete arg.

    """
    for word in words[0]:
        sent_so_far = " ".join([incomplete, word])
        try:
            all_possibilities(sent_so_far, words[1:])
        except IndexError:
            sentence_combos.append(sent_so_far.strip())
    return sentence_combos


def calculate_possibilities(choices: List[List[Text]]) -> int:
    """Calculates the possible sentences from 'choices'. Returns Integer."""
    possibilities = [len(el) for el in choices]
    return reduce(operator.mul, possibilities)


def change_word(word: Text, choices: List[Text]) -> Text:
    """Choose a word from 'choices' different from 'word'. Returns String."""
    choices.remove(word)
    return random.choice(choices)


def count_choices(list_: List[List[Text]]) -> List[int]:
    """Counts options for each element in 'list_'. Returns List."""
    return [len(el) for el in list_]


def get_sent_choice(choice: int, sentences: List[Text]) -> Text:
    """Gets the chosen sentence. Returns String."""
    return sentences[choice - 1][1]


def tag_bigrams(sentence: Text) -> List[Tuple[Text, Text]]:
    """Creates bigrams of pos_tags. Returns List of Tuples."""
    tagged = pos_tag(word_tokenize(sentence))
    tags = [tag[1] for tag in tagged]
    return list(bigrams(tags))


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


# duplicate of pos_tags()?
def only_tags(sent: Text) -> List[Text]:
    """Gets only the tags of 'sent'. Returns List."""
    tokens = word_tokenize(sent)
    tags = pos_tag(tokens)
    return [tag[1] for tag in tags]


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
    # get user choice
    sentence_choice = get_sent_choice(choice, sents)
    # bigrams of original sentence.
    print("Orignal sent bigrams:", tag_bigrams(sentence_choice))
    # tokenize
    tokens = word_tokenize(sentence_choice)
    # tag with part of speech
    tagged = pos_tag(tokens)
    # get pos words
    pos_tagged = pos_tag_word_list(tagged)
    # remove tags from list
    no_tags = remove_tags(pos_tagged)
    # remove empty elements from list
    cleaned_list = remove_empty_elements(no_tags)
    # show total sentence possibilities
    print("Possible sentences:", calculate_possibilities(cleaned_list))
    # show possible sentences. Could be in the billions.
#     print(calculate_possibilities(cleaned_list))
    # get only pos_tags
#     print("Only tags:", only_tags(sentence_choice))
    # show bigrams
#     print("Bigrams:", tag_bigrams(sentence_choice))

#    prompt user to choose to go on, in case too many sentences.

    # make list of possible sentences
    possible = all_possibilities("", cleaned_list)
    good_sents = []
    bad_sents = []
    for sent in possible[:100]:
        print(sent, tag_bigrams(sent))
        if syntactically_correct(sent, VALID_BIGRAMS):
            good_sent.append(sent)
        else:
            bad_sents.append(sent)

#     pprint(good_sents)
#     pprint(bad_sents)
    print("Good:", len(good_sents))
    print("Bad:", len(bad_sents))

#     pprint(possible[:30])

# TESTING
#     print(cleaned_list)

# everything is working before this line

    # TODO:
        # filter the sentences based on grammar rules
        # filter the sentences based on semantic rules
        # save all the sentence possibilities to a text file





def remove_empty_elements(list_: List[List[Text]]) -> List[List[Text]]:
    """Remove the empty elements. Returns List."""
    return [item for item in list_ if len(item) != 0]


def remove_simple_punctuation_tags(list_: List[Text]) -> List[Text]:
    """Removes the punctuation tags from 'list_'. Returns List"""
    return [item for item in list_ if item not in PUNCTUATION]


def remove_tags(list_: List[Text]) -> List[Text]:
    """Removes the word tags from 'list_'. Returns List"""
    return [item for item in list_ \
            if item not in TAG_LIST and item not in PUNCTUATION]


def syntactically_correct(sentence: Text, valid_bigrams: 
                          List[Tuple[Text, Text]]) -> bool:
    """Determines 'sentence' has correct grammatical structure. 
       Returns Boolean."""
    pairs = tag_bigrams(sentence)
    return all([pair in valid_bigrams for pair in pairs])


def valid_bigram_pair(pair: Tuple[Text, Text]) -> bool:
    """Checks if 'pair' is valid. Returns Boolean."""
    return pair in VALID_BIGRAMS


if __name__ == "__main__":
    sentences = list(enumerate(load_file(SENTENCE_FILE), start=1))
    vocabulary = load_file(VOCABULARY_FILE)
    main(vocabulary, sentences)
