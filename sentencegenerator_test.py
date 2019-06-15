"""sentencegen.py test module"""
# stand lib
from itertools import permutations
from pathlib import Path

# 3rd party
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.util import bigrams

# custom
from constants import *
from sentencegenerator import *

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
    sentence2 = "No, I'm not."
    tokens = word_tokenize(sentence)
    
    def test_nltk_word_tokenize(self):
        assert self.tokens == ["I", "am", "a", "coconut", "."]

    def test_nltk_pos_tag(self):
        tagged = pos_tag(self.tokens)
        assert tagged == [('I', 'PRP'), ('am', 'VBP'), ('a', 'DT'),
                          ('coconut', 'NN'), ('.', '.')]

class TestMainFunctions():
    sentence = "I am a coconut."
    tags = ['PRP', 'VBP', 'DT', 'NN', '.']
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    pos_tagged = pos_tag_word_list(tagged)
    no_tags = remove_tags(pos_tagged)
    only_word_choices = remove_empty_elements(no_tags)

    def test_sent_pos_tags(self):
        tokens = pos_tag(self.tokens)
        assert self.tags == pos_tags(tokens)

    def test_only_tags(self):
        assert only_tags(self.sentence) == ['PRP', 'VBP', 'DT', 'NN', '.']

    def test_get_sent_choice(self):
        list_ = [(1, "apple"), (2, "banana"), (3, "carrot")]
        assert get_sent_choice(2, list_) == "banana"
        assert get_sent_choice(3, list_) == "carrot"

    def test_change_word(self):
        for x in range(100):
            choices = self.tokens.copy()
            word = choices[0]
            assert change_word(word, choices) != word

    def test_pos_tag_word_list(self):
        combos = pos_tag_word_list(self.tagged)
        assert isinstance(combos, list)
        assert isinstance(combos[0], list)

    def test_load_tag_file(self):
        for tag in self.tagged:
            assert isinstance(load_file("tagdata/" + tag[1] + ".txt"), list)
#         assert len(load_file("tagdata/" + tag[1] + ".txt")) > 0

#     def test_

    def test_remove_simple_punctuation_tags(self):
        tags = ['PRP', 'VBP', 'DT', 'NN']
        assert tags == remove_simple_punctuation_tags(self.tags)

    def test_remove_tags(self):
        one_tag = ['.']
        assert remove_tags([]) == []
        assert remove_tags(one_tag) == []
        assert remove_tags(self.tags) == []
        assert remove_tags([["I", "am"], "a", ["coconut"], "."]) == \
                [["I", "am"], "a", ["coconut"]]

    def test_all_elements_are_list_type(self):
        some_not_lists = [["I", "am"], "a", ["coconut"], "."]
        normal = [["I"], ["am"], ["a"], ["coconut"], ["."]]
        assert all_elements_are_list_type([])
        assert all_elements_are_list_type(some_not_lists) == False
        assert all_elements_are_list_type(normal)

    def test_is_list_type(self):
        assert is_list_type([])
        assert is_list_type(["I"])
        assert is_list_type("I") == False
        assert is_list_type([["I"], ["am"], ["a"], ["coconut"], ["."]])

    def test_count_choices(self):
        assert count_choices([]) == []
        assert count_choices([self.tags]) == [5]
        assert count_choices([["I", "am"], ["a", "coconut"]]) == [2,2]

    def test_remove_empty_elements(self):
        assert remove_empty_elements([]) == []
        assert remove_empty_elements(["I"]) == ["I"]
        assert remove_empty_elements([["I"], [], ["am"]]) == [["I"], ["am"]]
    
    def test_calculate_possibilities(self):
        total = calculate_possibilities(self.only_word_choices)
        assert isinstance(total, int)

    def test_tag_bigrams(self):
        assert tag_bigrams(self.sentence) == \
               [('PRP', 'VBP'), ('VBP', 'DT'), ('DT', 'NN'), ('NN', '.')]

    def test_valid_bigram_pair(self):
        assert valid_bigram_pair([]) == False
        assert valid_bigram_pair(('PRP', 'VBP'))
        assert valid_bigram_pair(('VBP', 'DT'))
        assert valid_bigram_pair(('DT', 'NN'))
        assert valid_bigram_pair(('NN', '.'))

    def test_syntactically_correct(self):
#         valid_bigrams = tag_bigrams(self.sentence)
        assert syntactically_correct(self.sentence, VALID_BIGRAMS) 
