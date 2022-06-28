from packages import utils

notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

write_to_file =[]

for lines in notes:
    removed_punctuation = utils.remove_punctuation(lines)
    unigram = (utils.generate_n_grams(removed_punctuation, 1))
    bigram = (utils.generate_n_grams(removed_punctuation, 2))
    trigram = (utils.generate_n_grams(removed_punctuation, 3))
    write_to_file.append(utils.ngram_dict(lines, unigram, bigram, trigram))

columns = write_to_file[0].keys()

utils.write_csv(write_to_file, columns, 'result.csv')