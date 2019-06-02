"""sentencegen.py test module"""
from pathlib import Path
from sentencegen import *


class TestFiles():
    sentence_file = "grade2sentences.txt"
    vocabulary_file = "grade2vocab.txt"

    def test_sentence_pattern_files_exist(self):
        assert Path(self.sentence_file).exists() == True

    def test_vocabulary_files_exist(self):
        assert Path(self.vocabulary_file).exists() == True

    def test_load_files_sentences(self):
        sentences = load_files(self.sentence_file)
        assert (len(sentences) == 30) == True

    def test_load_files_vocabulary(self):
        vocabulary = load_files(self.vocabulary_file)
        assert (len(vocabulary) == 503) == True

class TestNltkMethods():
    pass
