# python script from https://github.com/aparrish/rwet/blob/master/ngrams-and-markov-chains.ipynb
# just for learning purposes

from collections import Counter
import random

# text = open("genesis.txt").read()
# words = text.split()
# pairs = []
# for i in range(len(words)-1):
#     this_pair = (words[i], words[i+1])
#     pairs.append(this_pair)
# # print pairs
# pair_counts = Counter(pairs)
# # print pair_counts.most_common(10)
# print pair_counts[("And","God")]
# print sum(pair_counts.values())
# print pair_counts[("And","God")] / sum(pair_counts.values())

# char_pairs = [(text[i], text[i+1]) for i in range(len(text)-1)]
# # print char_pairs
# pair_counts = Counter(char_pairs)
# print pair_counts.most_common(10)

# seven_grams = [tuple(words[i:i+7]) for i in range(len(words)-6)]
# print seven_grams[:10]

def ngrams_for_sequence(n, seq):
    return [tuple(seq[i:i+n]) for i in range(len(seq)-n+1)]

# genesis_9grams = ngrams_for_sequence(9, text)
# print random.sample(genesis_9grams, 10)
# word_5grams = ngrams_for_sequence(5,open("genesis.txt").read().split())
# print word_5grams

# print ngrams_for_sequence(2, "condescendences")

# Markov models: what comes next?
# src = "condescendences"
# src += "$"
# model = {}
# for i in range(len(src)-2):
#     ngram = tuple(src[i:i+2])
#     next_item = src[i+2]
#     if ngram not in model:
#         model[ngram] = []
#     model[ngram].append(next_item)
# print model

def  add_to_model (model, n, seq):
    # make a copy of seq and append None to the end
    seq = list(seq[:]) + [None]
    for i in range(len(seq)-n):
        # tuple because we're using it as a dict key!
        gram = tuple(seq[i:i+n])
        next_item = seq[i+n]
        if gram not in model:
            model[gram] = []
        model[gram].append(next_item)

def markov_model(n, seq):
    model = {}
    add_to_model(model, n, seq)
    return model

# print markov_model(2,"condescendences")
# genesis_markov_model = markov_model(3,open("genesis.txt").read().split())
# print genesis_markov_model[('and', 'over', 'the')]

cmodel = markov_model(2,"condescendences")
output = "co"
for i in range(100):
    ngram = tuple(output[-2:])
    next_item = random.choice(cmodel[ngram])
    if next_item is None:
        break
    else:
        output += next_item
    # print output

def gen_from_model(n, model, start=None, max_gen=100):
    if start is None:
        start = random.choice(list(model.keys()))
    output = list(start)
    for i in range(max_gen):
        start = tuple(output[-n:])
        next_item = random.choice(model[start])
        if next_item is None:
            break
        else:
            output.append(next_item)
    return output

# print ''.join(gen_from_model(2, cmodel, ('c', 'o')))

# sea_model = markov_model(3, "she sells seashells by the seashore")
# print sea_model
# for i in range(10):
#     print ''.join(gen_from_model(3, sea_model,('s','h','e')))

# Advanced Markov style: Generating lines
# genesis_word_model = markov_model(2, open("genesis.txt").read().split())
# generated_genesis = " ".join(gen_from_model(2, genesis_word_model,('In','the'),500))
# print generated_genesis

def markov_model_from_sequences(n, sequences):
    model = {}
    for item in sequences:
        add_to_model(model, n, item)
    return model

genesis_lines = open("genesis.txt").readlines()

genesis_lines_words = [line.strip().split() for line in genesis_lines]
genesis_lines_model = markov_model_from_sequences(2, genesis_lines_words)

for i in range(10):
    print("verse", i, "-", ' '.join(gen_from_model(2, genesis_lines_model)))
