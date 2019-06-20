"""Get a list of randomized sentences."""
# stand lib
from pathlib import Path
from pprint import pprint
import random
from typing import List
from typing import Text

# 3rd party
from nltk.tokenize import word_tokenize


def load_file(path_: Text) -> List[Text]:
    """Load a files lines as elements. Returns List."""
    with open(path_, "r") as f:
        return [line.strip() for line in f.readlines()]


def file_paths(dir_path: Text) -> List[Text]:
    """Load file names as elements. Returns List."""
    return [name for name in Path(dir_path).iterdir()]

def main(dirs: List[Text]) -> None:
    all_sentences = []
    for dir_ in dirs:
        files = file_paths(dir_)
        temp = [load_file(file_) for file_ in files]
        flat_list = set([sent for sublist in temp for sent in sublist])  # set of all sentences
        all_sentences += flat_list
    rankings = sorted([(difficulty_rank(sent), sent) for sent in all_sentences])
    with open("rankings.txt", "a+") as f:
        while len(rankings) > 2:
            temp = []
            #1
            choice = random.choice(rankings)
            temp.append(choice)
            rankings.remove(choice)
            #2
            choice = random.choice(rankings)
            temp.append(choice)
            rankings.remove(choice)
            #3
            choice = random.choice(rankings)
            temp.append(choice)
            rankings.remove(choice)
            for line in sorted(temp):
                f.write(str(line) + "\n")
            f.write("\n")


def difficulty_rank(sentence: Text) -> int:
    """Calculates 'sentence' difficulty level. Returns Integer."""
    chars = len(sentence)
    words = len(word_tokenize(sentence))
    return words + (chars//5)


if __name__ == "__main__":
    dirs = [
        "/Users/wandalcooper/Programming/EnglishData/totalenglish/grade1sentences",
        "/Users/wandalcooper/Programming/EnglishData/totalenglish/grade2sentences",
        ]
    main(dirs)

