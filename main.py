from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

line_wise_ngram = []
all_n_gram = []
n_grams_with_freq = []
n_gram_string = []
all_clean_lines = []
write_this = []
top_20_ngram = []

count = 0
for lines in notes:
    words = []
    temp = []
    clean = utils.remove_punctuation(lines)
    text = clean.split('--')[0].split()
    line = [word for word in text if word not in utils.en_stopwords]
    temp.append(' '.join(line))
    line_wise_ngram.append(utils.generate_n_grams(temp, 1))
    line_wise_ngram[count].extend(utils.generate_n_grams(temp, 2))
    line_wise_ngram[count].extend(utils.generate_n_grams(temp, 3))
    all_clean_lines.append(' '.join(line))
    count+=1

ngrams_str_linewise = []
for i in range(len(line_wise_ngram)):
    x = []
    for items in line_wise_ngram[i]:
        x.append(" ".join(items))
    ngrams_str_linewise.append(x)


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
    current_ngram = []
    for items in ngrams_str_linewise[i]:
        if items in top_20_ngram:
            current_ngram.append(items)
    write_this.append({
        'ngrams': ",".join(set(current_ngram)),
        "Notes": notes[i]
    })
    
utils.write_csv('notes_with_ngrams.csv', write_this, write_this[0].keys())