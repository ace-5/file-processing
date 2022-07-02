from packages import utils
notes = utils.read_csv('govt_urls_state_only.csv', 'Note')

uni = []
bi = []
tri = []
line_wise_ngram = []
for line in notes:
    clean_line = utils.clean_line(line)
    line_uni = utils.generate_n_grams([clean_line], 1)
    line_bi = utils.generate_n_grams([clean_line], 2)
    line_tri = utils.generate_n_grams([clean_line], 3)
    this_line_ngram = line_uni+line_bi+line_tri
    uni+=line_uni
    bi+=line_bi
    tri+=line_tri
    add_to_list = []
    for items in this_line_ngram:
        add_to_list.append(" ".join(items))
    line_wise_ngram.append(add_to_list)

top_n_gram = []
top_n_gram+=utils.get_top_ngrams(uni, 20)
top_n_gram+=utils.get_top_ngrams(bi, 20)
top_n_gram+=utils.get_top_ngrams(tri, 20)


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