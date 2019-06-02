"""sentencegen.py test module"""
from pathlib import Path

class TestFiles():
    sentences = "grade2sentences.txt"
    vocabulary = "grade2vocab.txt"
    def test_sentence_pattern_files_exist(self):
        assert Path(self.sentences).exists() == True

    def test_vocabulary_files_exist(self):
        assert Path(self.vocabulary).exists() == True
