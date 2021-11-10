from possible_tag_bigrams import possible_bigrams
from custom_bigram_rules import valid_bigrams
BIGRAM_LIST = possible_bigrams
CHOICE_MESSAGE = "Choose a sentence number. "
NOT_A_NUMBER_ERROR = "Please choose a valid number."
SENTENCE_FILE = "grade2sentences.txt"
VOCABULARY_FILE = "grade2vocab.txt"
PUNCTUATION = [".", ",", "?",]
PUNCTUATION_TAGS = [".", ",", "?",]
TAG_LIST = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
            "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP",
            "RB", "RBR", "RBS", "RP", "TO", "UH", "VB", "VBD", "VBG",
            "VBN", "VBP", "VBZ", "WDT", "WP", "WP", "WRB"]
VALID_BIGRAMS = valid_bigrams
WELCOME_MESSAGE = "Simple Sentence Generator. Press enter..."
