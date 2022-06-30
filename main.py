from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

unigram =[]
bigram =[]
trigram =[]
top_ngram = []
all_clean_lines = []
json_dict = {
    "Unigram": {},
    "Bigram": {},
    "Trigram": {},
    "Notes with top n_gram": {}
    }

def make_json(key, ngram, n=20):
    for k,v in utils.n_gram_freq(ngram, n):
        json_dict[key][k] = v

def all_top_ngrams(ngram):        
    for items in json_dict[ngram].keys():
        top_ngram.append(items[2:-2].replace('\'', '').replace(' ', '').split(','))

for lines in notes:
    clean = utils.remove_punctuation(lines)
    text = clean.split()
    words = [word for word in text if word.lower() not in utils.en_stopwords]
    unigram.extend(utils.generate_n_grams(words[:-4], 1))
    bigram.extend(utils.generate_n_grams(words[:-4], 2))
    trigram.extend(utils.generate_n_grams(words[:-4], 3))
    clean_line = ''
    for i in range(len(words)):
        clean_line += (words[i]+' ')
    all_clean_lines.append(clean_line)

make_json('Unigram', unigram)
make_json('Bigram', bigram)
make_json('Trigram', trigram)

for items in json_dict['Unigram'].keys():
    top_ngram.append(items[2:-2].replace('\'', '').replace(',', ''))
for items in json_dict['Bigram'].keys():
    top_ngram.append(items[2:-2].replace('\'', '').replace(',', ''))
for items in json_dict['Trigram'].keys():
    top_ngram.append(items[2:-2].replace('\'', '').replace(',', ''))


for ngram in top_ngram:
    count = 0
    for line in all_clean_lines:
        if (' '+ngram+' ') in line:
            if f'{ngram}' not in json_dict['Notes with top n_gram'].keys():
                json_dict['Notes with top n_gram'][f'{ngram}'] = []
            json_dict['Notes with top n_gram'][f'{ngram}'].append(notes[count])
        count +=1

utils.write_json('result.json', json_dict)
