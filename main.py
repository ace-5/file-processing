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
clean_top_ngram = utils.remove_state_name(top_n_gram)


write_this = []
for i in range(len(notes)):
    current_ngram = []
    current_state = []
    for items in line_wise_ngram[i]:
        if items in clean_top_ngram:
            current_ngram.append(items)
        if items in utils.states_lwr:
            current_state.append(items.title())
    write_this.append({
        'ngrams': ",".join(set(current_ngram)),
        'state': ", ".join(set(current_state)),
        "Notes": notes[i]
    })

utils.write_csv('notes_with_ngrams_and_state_name.csv', write_this, write_this[0].keys())