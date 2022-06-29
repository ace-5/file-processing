from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

unigram =[]
bigram =[]
trigram =[]
json_dict = {
    "Unigram": {},
    "Bigram": {},
    "Trigram": {}
    }

def make_json(key, ngram, n=20):
    for k,v in utils.n_gram_freq(ngram, n):
        json_dict[key][k] = v

for lines in notes:
    clean = utils.remove_punctuation(lines)
    text = clean.split()
    unigram.extend(utils.generate_n_grams(text[:-4], 1))
    bigram.extend(utils.generate_n_grams(text[:-4], 2))
    trigram.extend(utils.generate_n_grams(text[:-4], 3))

make_json('Unigram', unigram)
make_json('Bigram', bigram)
make_json('Trigram', trigram)


utils.write_json('result.json', json_dict)
