from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

top_n_gram = []
unigram =[]
bigram =[]
trigram =[]
all_clean_lines = []
main_dict = {
    "Unigram": [],
    "Bigram": [],
    "Trigram": []
}
write_this = []

def add_to_main_dict(key, ngram):
    for k,v in utils.n_gram_freq(ngram):
        main_dict[key].append([k, v])

def add_to_top_ngram(ngram, main_dict, n=20): 
    for item, freq in main_dict[ngram][:20]:
        top_n_gram.append(item[2:-2].replace('\'', '').replace(',', ''))

# loop to remove punctuations and stopwords from Note column
# append each cleaned line to new list 
for lines in notes:
    clean = utils.remove_punctuation(lines)
    text = clean.split()
    words = [word for word in text if word.lower() not in utils.en_stopwords]
    unigram.extend(utils.generate_n_grams(words[:-4], 1))
    bigram.extend(utils.generate_n_grams(words[:-4], 2))
    trigram.extend(utils.generate_n_grams(words[:-4], 3))
    all_clean_lines.append(' '.join(words))

add_to_main_dict('Unigram', unigram)
add_to_main_dict('Bigram', bigram)
add_to_main_dict('Trigram', trigram)

add_to_top_ngram('Unigram', main_dict)
add_to_top_ngram('Bigram', main_dict)
add_to_top_ngram('Trigram', main_dict)


# Iterate over every Note columns value
for i in range(len(all_clean_lines)):
    # declare and initialize required variable before every iteration
    unigram_list = []
    bigram_list = []
    trigram_list = []        
    write_this.append({
        'Note': str,
        'Unigram': str,
        'Bigram': str,
        'Trigram': str
    })
    # assign current line to Note key of ith item 
    write_this[i]['Note'] = notes[i]

    # make a list of ngrams that occur in current line 
    # join that list by , as seperator
    unigram_list.extend([ngram for ngram in top_n_gram[:20] if " "+ngram+" " in ' '+all_clean_lines[i]+' '])
    write_this[i]['Unigram'] = ','.join(unigram_list)
    bigram_list.extend([ngram for ngram in top_n_gram[20:40] if " "+ngram+" " in ' '+all_clean_lines[i]+' '])
    write_this[i]['Bigram'] = ','.join(bigram_list)
    trigram_list.extend([ngram for ngram in top_n_gram[40:] if " "+ngram+" " in ' '+all_clean_lines[i]+' '])
    write_this[i]['Trigram'] = ','.join(trigram_list)

# write the prepared list to file 
utils.write_csv('notes_with_ngrams.csv', write_this, write_this[0].keys())
