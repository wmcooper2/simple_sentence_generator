# stand lib
from pathlib import Path

# custom
from sentencerank import *
from personal import DIRS

# not real examples
test_data = [
    ("45","I committed coconut genocide in retaliation."),
    ("13","I like bananas."),
    ("22","A coconut ate my banana yesterday."),
    ("17","I eat many bananas."),]

just_sents = [
    ("I committed coconut genocide in retaliation."),
    ("I like bananas."),
    ("A coconut ate my banana yesterday."),
    ("I eat many bananas."),]

def test_file_paths():
    assert isinstance(file_paths(DIRS[0]), list)

def test_difficulty_levels():
    EASY, MEDIUM, HARD = 8, 14, 19
    easy = difficulty_levels(test_data, EASY, MEDIUM)
    medium = difficulty_levels(test_data, MEDIUM, HARD)
    hard = difficulty_levels(test_data, HARD, 1000)
    assert len(easy) == 1
    assert len(medium) == 1
    assert len(hard) == 2

def test_difficulty_rank():
    assert difficulty_rank("I like eat coconuts.") == 9

def test_get_unique_sentence():
    choice = get_unique_sentence(just_sents)
    assert choice
    assert choice not in just_sents

def test_rank_sentences():
    pass

def test_group_of_3():
    assert group_of_3(test_data[:3]) == \
    [("13","I like bananas."),
    ("22","A coconut ate my banana yesterday."),
    ("45","I committed coconut genocide in retaliation."),]
