from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

line_wise_ngram = []
n_grams_with_freq = []
write_this = []
top_20_ngram = []
# loop to collect ngarms line wise
for i in range(len(notes)):
    clean = utils.remove_punctuation(notes[i])
    text = clean.split('--')[0].split()
    line = [word for word in text if word not in utils.en_stopwords]
    line_str = ' '.join(line)
    line_wise_ngram.append(utils.generate_n_grams(line_str, 1))
    line_wise_ngram[i].extend(utils.generate_n_grams(line_str, 2))
    line_wise_ngram[i].extend(utils.generate_n_grams(line_str, 3))

# append all ngrams in specific line to common list for that line
ngrams_str_linewise = []
for i in range(len(line_wise_ngram)):
    x = []
    for items in line_wise_ngram[i]:
        x.append(" ".join(items))
    ngrams_str_linewise.append(x)

# collect top 20 of each ngrams to a common list
top_20_ngram.extend(ngram for ngram, freq in n_grams_with_freq[0][:20])
top_20_ngram.extend(ngram for ngram, freq in n_grams_with_freq[1][:20])
top_20_ngram.extend(ngram for ngram, freq in n_grams_with_freq[2][:20])

# compare if ngrams of current line is in top n-gram
# When True: join all unique ngrams of that line, which are present in top 20, together as string
# append to list which contains dict as it's item
# each dict contains original line and it's ngram in top n gram 
for i in range(len(notes)):
    current_ngram = []
    for items in ngrams_str_linewise[i]:
        if items in top_20_ngram:
            current_ngram.append(items)
    write_this.append({
        'ngrams': ",".join(set(current_ngram)),
        "Notes": notes[i]
    })

utils.write_csv('notes_with_ngrams.csv', write_this, write_this[0].keys())