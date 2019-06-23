"""Get a list of randomized sentences."""
# stand lib
from pathlib import Path
from pprint import pprint
import random
from typing import List
from typing import Text
from typing import Tuple

# 3rd party
from nltk.tokenize import word_tokenize

# custom
from personal import DIRS


def difficulty_levels(all_sents: List[Text],
                      low: int, 
                      high: int) -> List[Text]:
    """Divides sentences into a difficulty level. Returns List."""
    return [sent[1] for sent in all_sents if low <= int(sent[0]) and int(sent[0]) <= high]


def difficulty_rank(sentence: Text) -> int:
    """Calculates 'sentence' difficulty level. Returns Integer."""
    chars = len(sentence)
    words = len(word_tokenize(sentence))
    return words + (chars//5)


def file_paths(dir_path: Text) -> List[Text]:
    """Load file names as elements. Returns List."""
    return [name for name in Path(dir_path).iterdir()]


def get_unique_sentence(all_sents: List[Text]) -> Text:
    """Chooses unique sentence from 'all_sents'. Modifies 'all_sents'. Returns String."""
    choice = random.choice(all_sents)
    all_sents.remove(choice)
    return choice


def group_of_3(sents: List[Tuple[int, Text]]) -> List[Text]:
    """Makes a group of 3 sentences. Returns List."""
    return sorted(sents, key=lambda x: x[0])


def load_file(path_: Text) -> List[Text]:
    """Load a files lines as elements. Returns List."""
    with open(path_, "r") as f:
        return [line.strip() for line in f.readlines()]


def load_files(dirs: List[Text]) -> List[Text]:
    """Loads all files. Returns List."""
    temp = []
    for dir_ in dirs:
        files = file_paths(dir_)
        file_ = [load_file(file_) for file_ in files]
        flat_list = set([sent for sublist in file_ for sent in sublist])
        temp += flat_list
    return temp


def rank_sentences(all_sents:List[Text]) -> List[Tuple[int, Text]]:
    """Ranks the sentences. Returns sorted List of Tuples."""
    return sorted([(difficulty_rank(sent), sent) for sent in all_sents])


def main(dirs: List[Text]) -> None:
    temp = load_files(dirs)
    rankings = rank_sentences(temp)

    EASY, MEDIUM, HARD = 8, 14, 19
    easy = difficulty_levels(rankings, EASY, MEDIUM)
    medium = difficulty_levels(rankings, MEDIUM, HARD)
    hard = difficulty_levels(rankings, HARD, 1000)

    # need 40 groups for 40 cards
    save_to = "rankings.txt"
    with open(save_to, "w+") as f:
        for x in range(40):
            group = [
                    get_unique_sentence(easy),
                    get_unique_sentence(medium),
                    get_unique_sentence(hard),]

            # write as a group of 3
            for line in group:
                f.write(str(line) + "\n")
            f.write("\n")


if __name__ == "__main__":
    main(DIRS)
