"""sentencegen.py; generate sentences based on given sentence structure and a given vocabulary."""
# stand lib
from pathlib import Path
from typing import Text
from typing import List

# 3rd party
# import nltk

sentence_file = "grade2sentences.txt"
vocabulary_file = "grade2vocab.txt"
sentences = []
vocabulary = []


def load_files(file_: Text) -> List[Text]:
    try:
        temp = []
        with open(file_, "r") as f:
            for line in f.readlines():
                temp.append(line.strip())
        return temp
    except FileNotFoundError:
        return []



# tokenize/parse the sentence
# determine the parts of speech
    # make list of the needed parts of speech
# load vocabulary
    # make list of the parts of speech of the vocabulary
# make random sentences by only using the given sentence pattern and vocab


def main():
    # User is presented with a list of sentence choices.
    # User chooses one with a number
    # When User makes a choice, program asks for an amount.
        # if the user makes a mistake, then the options are presented again
    # Program makes a text file with the amount of sentences requested.
    pass

if __name__ == "__main__":
    main()
