"""sentencegen.py test module"""
from itertools import permutations
from pathlib import Path
from sentencegen import *
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


class TestFiles():
    sentence_file = "grade2sentences.txt"
    vocabulary_file = "grade2vocab.txt"

    def test_load_file_sentences(self):
        sentences = load_file(self.sentence_file)
        assert Path(self.sentence_file).exists()
        assert len(sentences) == 30
        assert sentences[0] == "I was happy."

    def test_load_file_vocabulary(self):
        vocabulary = load_file(self.vocabulary_file)
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
    sentence = "I am a coconut."
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    def test_sent_pos_tags(self):
        tokens = pos_tag(self.tokens)
        tags = ['PRP', 'VBP', 'DT', 'NN', '.']
        assert tags == pos_tags(tokens)

    def test_get_sent_choice(self):
        list_ = [(1, "apple"), (2, "banana"), (3, "carrot")]
        assert get_sent_choice(2, list_) == "banana"
        assert get_sent_choice(3, list_) == "carrot"

    def test_change_word(self):
        for x in range(100):
            choices = self.tokens.copy()
            word = choices[0]
            assert change_word(word, choices) != word
