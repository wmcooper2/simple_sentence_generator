from pprint import pprint

sub = ["I", "He"]
verb = ["like", "likes"]
obj = ["birds", "cats"]

poss = [sub, verb, obj]
allsentences = []

def recfun(string, list_):
    for word in list_[0]:
        sent_so_far = " ".join([string, word])
        try:
            recfun(sent_so_far, list_[1:])
        except IndexError:
            allsentences.append(sent_so_far.strip())

# breakpoint()
recfun("", poss)
pprint(allsentences)
