import csv
from nltk.corpus import stopwords
import string

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
        if letter in string.punctuation:
            continue
        returnline += letter
    
    return returnline

def generate_n_grams(text, n_gram):
    n_gram_result = []
    words = text.split()
    words = [word for word in words if word.lower() not in en_stopwords]
    for i in range(len(words)-n_gram+1):
            n_gram_result.append(words[i:i+n_gram])
    return n_gram_result

def ngram_dict(line, unigram, bigram, trigram):
    return({
        "Raw": line,
        "Unigram": unigram,
        "Bigram": bigram,
        "Trigram": trigram
    })

def write_csv(to_write, columns, filename):
    with open (filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(to_write)
