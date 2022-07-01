from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

top_20_ngram = []
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
    text = clean.split('--')[0].split()
    line = [word for word in text if word not in utils.en_stopwords]
    all_clean_lines.append(' '.join(line))

# change 3 to 'n' to obtain grams from unigram to n-gram 
# loop to manage internal variables and data structure
for i in range(3):
    temp = []
    all_n_gram.append(utils.generate_n_grams(all_clean_lines, i+1))
    for items in all_n_gram[i]:
        temp.append(" ".join(items))
    n_gram_string.append(temp) 
    n_grams_with_freq.append(utils.n_gram_freq(n_gram_string[i]))

top_20_ngram.extend(ngram for ngram, freq in n_grams_with_freq[0][:20])
top_20_ngram.extend(ngram for ngram, freq in n_grams_with_freq[1][:20])
top_20_ngram.extend(ngram for ngram, freq in n_grams_with_freq[2][:20])

for i in range(len(notes)):
    line = [all_clean_lines[i]]
    temp = []
    line_ngram_string = []
    line_ngram = []
    note = notes[i]
# generate n grams for each line
# TODO: Make a function to generate and return joined string
    line_ngram.extend(utils.generate_n_grams(line, 1))
    line_ngram.extend(utils.generate_n_grams(line, 2))
    line_ngram.extend(utils.generate_n_grams(line, 3))
    
    for items in line_ngram:
        line_ngram_string.append(" ".join(items))
    
    for items in line_ngram_string:
        if items in top_20_ngram:
            temp.append(items)
    
    temp = set(temp)
    ngrams = ', '.join(temp)
    write_this.append({
        'ngrams': ngrams,
        'Note': note
    })

# write the prepared list to file 
utils.write_csv('notes_with_ngrams.csv', write_this, write_this[0].keys())