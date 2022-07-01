import csv
from nltk.corpus import stopwords
import string
import json


en_stopwords = stopwords.words('english')

def read_csv(file_name, col_name):
    result = []
    with open(file_name) as f:
        file_items = csv.DictReader(f)
        for row in file_items:
            result.append(row[col_name])
    return result

def remove_punctuation(line):
    returnline = ''
    for letter in line:
        if letter in string.punctuation.replace('-', ''):
            continue
        returnline += letter
    lower = returnline.lower()
    return lower

def generate_n_grams(all_lines, ngram):
    n_gram_result = []
    for line in all_lines:
        line = line.split()
        for i in range(len(line)-ngram+1):
            n_gram_result.append(line[i:i+ngram])
    return n_gram_result


def n_gram_freq(ngram):
    """
    Returns ngram along with it's frequency in descending order
    """
    frequency = {}
    for items in ngram:
        if items not in frequency.keys():
            frequency[items] = 1
        else:
            frequency[items] += 1

    return (list(sorted(frequency.items(), key =
                lambda kv:(kv[1], kv[0]), reverse= True)))
            


def write_csv(filename, to_write, columns):
    with open (filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(to_write)


def write_json(filename, json_dict):
    with open (filename, 'w') as f:
        writer = json.dumps(json_dict, indent=2, ensure_ascii = False)
        f.write(writer)


