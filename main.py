from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')


all_n_gram = []
n_grams_with_freq = []
n_gram_string = []
all_clean_lines = []
write_this = []



# loop to remove punctuations and stopwords from Note column
# append each cleaned line to new list 
for lines in notes:
    words = []
    clean = utils.remove_punctuation(lines)
    text = clean.split()
    for i in range(len(text)):
        if text[i]=='--':
            break
        elif text[i] in utils.en_stopwords:
            continue
        words.append(text[i])
    all_clean_lines.append(' '.join(words))

# change 3 to 'n' to obtain grams from unigram to n-gram 
# loop to manage internal variables and data structure
for i in range(3):
    all_n_gram.append(utils.generate_n_grams(all_clean_lines, i+1))
    n_gram_string.append([])
    for items in all_n_gram[i]:
        n_gram_string[i].append(" ".join(items))        
    n_grams_with_freq.append([])
    n_grams_with_freq[i] = utils.n_gram_freq(n_gram_string[i])


for i in range(len(all_clean_lines)):
    ngram_list = []        
    write_this.append({
        'ngrams': str,
        'Note': str
    })
    # assign current line to Note key of ith item 
    write_this[i]['Note'] = notes[i]

    # make a list of ngrams that occur in current line 
    # join that list by , as seperator
    ngram_list.extend([ngram for ngram, freq in n_grams_with_freq[0][:20] if " "+ngram+" " in ' '+all_clean_lines[i]+' '])
    ngram_list.extend([ngram for ngram, freq in n_grams_with_freq[1][:20] if " "+ngram+" " in ' '+all_clean_lines[i]+' '])
    ngram_list.extend([ngram for ngram, freq in n_grams_with_freq[2][:20] if " "+ngram+" " in ' '+all_clean_lines[i]+' '])
    write_this[i]['ngrams'] = ','.join(ngram_list)

# write the prepared list to file 
utils.write_csv('notes_with_ngrams.csv', write_this, write_this[0].keys())
