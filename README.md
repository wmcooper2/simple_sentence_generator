# Simple Sentence Generator
This is a CLI tool for generating simple sentences from a small set of sentences and a small set of vocabulary words.  
_Low priority project. I learned what I wanted to learn from this project and I don't intend to continue working on it._  

## Purpose
* To make a simple tool for generating a lot of sentences using the same part-of-speech structure as an input sentence.
* The user is expected to manually filter through the generated sentences to get a small collection of useful ones.
  * The intention is to ease the stress on one's creative skills and reduce the task to something simpler.



## Operation
### Setup
1. Make the program executable: `chmod 755 note.sh`  
2. Add a soft link to the executable to run it from anywhere:  
```bash
cd /usr/local/bin
ln -s <path to your executable> note
```

### Sentence Generator
1. Run: `python3 sentencegenerator.py`
2. Follow the instructions in the terminal.

### Sentence Difficulty Ranking
1. Run: `python3 sentencerank.py`
2. `ranking.txt` is written to `sentenceranking/`

### Tests
Run: `pytest -v **/*_test.py`.

### What I learned
* Just use the NLTK package's tools. It's much faster and easier.

## Notes
* If having an issue running the program such as "Resource punkt not found." then try this:  
```bash
python3
>>> import nltk
>>> nltk.download()
```
Then download the packages and rerun the program.

* This project is intended to be a tool for making semantically valid permutations based on a small subset of the whole English language.  
* So far, the permutations are created successfully but are mostly semantically invalid, so they require manual review.  

Assumptions:
1. The user provides a list of sentences with the patterns they are trying to recreate.
2. The user provides a list of vocabulary that they want to generate the sentences from.
3. The grammatical structure of each sentence is not changed. Only the individual words are changed.
4. The results produced are not 100% accurate and will require minimal review.
