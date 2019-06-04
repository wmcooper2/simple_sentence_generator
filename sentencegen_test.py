"""sentencegen.py test module"""
from pathlib import Path
from sentencegen import *
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


class TestFiles():
    sentence_file = "grade2sentences.txt"
    vocabulary_file = "grade2vocab.txt"

    def test_load_files_sentences(self):
        sentences = load_files(self.sentence_file)
        assert Path(self.sentence_file).exists()
        assert len(sentences) == 30
        assert sentences[0] == "I was happy."

    def test_load_files_vocabulary(self):
        vocabulary = load_files(self.vocabulary_file)
        assert Path(self.vocabulary_file).exists()
        assert len(vocabulary) == 503
        assert vocabulary[0] == "Africa"

class TestNltkMethods():
    sentence = "I am a coconut."
    tokens = word_tokenize(sentence)
    
    def test_nltk_word_tokenize(self):
        assert self.tokens == ["I", "am", "a", "coconut", "."]

    def test_nltk_pos_tag(self):
        tagged = pos_tag(self.tokens)
        assert tagged == [('I', 'PRP'), ('am', 'VBP'), ('a', 'DT'),
                          ('coconut', 'NN'), ('.', '.')]

class TestMainFunctions():

    def test_sent_pos_tags(self):
        # get pos tags
        assert pos_tags == ['PRP', 'VBP', 'DT', 'NN', '.']
