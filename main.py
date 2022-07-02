from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

clean_lines = []
line_wise_ngram = []
n_grams_freq = []
top_n_gram = []

for i in range(len(notes)):
    add_to_list = []
    clean = utils.remove_punctuation(notes[i])
    text = clean.split('--')[0].split()
    line = [word for word in text if word not in utils.en_stopwords]
    clean_lines.append(" ".join(line))
    this_line_ngram=utils.generate_n_grams([' '.join(line)], 1)
    this_line_ngram.extend(utils.generate_n_grams([' '.join(line)], 2))
    this_line_ngram.extend(utils.generate_n_grams([' '.join(line)], 3))
    for items in this_line_ngram:
        add_to_list.append(" ".join(items))
    line_wise_ngram.append(add_to_list)

for i in range(3):
    n_grams_freq.append(utils.n_gram_freq(utils.generate_n_grams(clean_lines, i+1)))

top_n_gram.extend(ngram for ngram, freq in n_grams_freq[0][:20])
top_n_gram.extend(ngram for ngram, freq in n_grams_freq[1][:20])
top_n_gram.extend(ngram for ngram, freq in n_grams_freq[2][:20])

write_this = []
for i in range(len(notes)):
    current_ngram = []
    for items in line_wise_ngram[i]:
        if items in top_n_gram:
            current_ngram.append(items)
    write_this.append({
        'ngrams': ",".join(set(current_ngram)),
        "Notes": notes[i]
    })

utils.write_csv('notes_with_ngrams.csv', write_this, write_this[0].keys())

