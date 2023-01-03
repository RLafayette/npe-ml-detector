import numpy as np
import re
import glob
import csv
from datasketch.minhash import MinHash
from datasketch.weighted_minhash import WeightedMinHashGenerator
from datasketch.lsh import MinHashLSH
from openpyxl import Workbook


samples_dict = {}

def analyse():
    analyse_correlation()
    analyse_cosine()
    analyse_euclidean()
    analyse_jaccard()
    convert_excel()

def analyse_correlation():
    sample_keys = samples_dict.keys()
    min_hashes = {}
    for key in sample_keys:
        min_hashes[key] = MinHash(num_perm=128)
        for d in samples_dict[key]:
            min_hashes[key].update(d.encode('utf8'))
    
    lsh = MinHashLSH(threshold=0.5, num_perm=128)
    for key in sample_keys:
        lsh.insert(key, min_hashes[key])

    result_matrix = {}

    for key in sample_keys:
        result_matrix[key] = {}
        for key2 in sample_keys:
            #print(key + " " + key2 + "\n")
            (result_matrix[key])[key2] = min_hashes[key].correlation(min_hashes[key2])
            #print(key + " " + key2 + "\n")
    write_csv("results/result_correlation.csv", result_matrix, sample_keys)

def analyse_cosine():
    sample_keys = samples_dict.keys()
    min_hashes = {}
    for key in sample_keys:
        min_hashes[key] = MinHash(num_perm=128)
        for d in samples_dict[key]:
            min_hashes[key].update(d.encode('utf8'))
    
    lsh = MinHashLSH(threshold=0.5, num_perm=128)
    for key in sample_keys:
        lsh.insert(key, min_hashes[key])

    result_matrix = {}

    for key in sample_keys:
        result_matrix[key] = {}
        for key2 in sample_keys:
            #print(key + " " + key2 + "\n")
            (result_matrix[key])[key2] = min_hashes[key].cosine(min_hashes[key2])
            #print(key + " " + key2 + "\n")
    write_csv("results/result_cosine.csv", result_matrix, sample_keys)

def analyse_euclidean():
    sample_keys = samples_dict.keys()
    min_hashes = {}
    for key in sample_keys:
        min_hashes[key] = MinHash(num_perm=128)
        for d in samples_dict[key]:
            min_hashes[key].update(d.encode('utf8'))
    
    lsh = MinHashLSH(threshold=0.5, num_perm=128)
    for key in sample_keys:
        lsh.insert(key, min_hashes[key])

    result_matrix = {}

    for key in sample_keys:
        result_matrix[key] = {}
        for key2 in sample_keys:
            #print(key + " " + key2 + "\n")
            (result_matrix[key])[key2] = min_hashes[key].euclidean(min_hashes[key2])
            #print(key + " " + key2 + "\n")
    write_csv("results/result_euclidean.csv", result_matrix, sample_keys)

def analyse_jaccard():
    sample_keys = samples_dict.keys()
    min_hashes = {}
    for key in sample_keys:
        min_hashes[key] = MinHash(num_perm=128)
        for d in samples_dict[key]:
            min_hashes[key].update(d.encode('utf8'))
    
    lsh = MinHashLSH(threshold=0.5, num_perm=128)
    for key in sample_keys:
        lsh.insert(key, min_hashes[key])

    result_matrix = {}

    for key in sample_keys:
        result_matrix[key] = {}
        for key2 in sample_keys:
            #print(key + " " + key2 + "\n")
            (result_matrix[key])[key2] = min_hashes[key].jaccard(min_hashes[key2])
            #print(key + " " + key2 + "\n")
    write_csv("results/result_jaccard.csv", result_matrix, sample_keys)


def write_csv(filename, matrix, fields):
    with open(filename, "w") as f:
        w = csv.DictWriter(f, fields)
        w.writeheader()
        for k in matrix:
            #w.writerow({field: matrix[k].get(field) or k for field in fields})
            w.writerow({field: matrix[k].get(field) for field in fields})

def convert_excel():
    csv_filepaths = glob.glob("results/*.csv")
    for filepath in csv_filepaths:
        wb = Workbook()
        ws = wb.active
        sample_filename = re.search(r"results\/(.+)\.csv", str(filepath)).group(1)
        with open(filepath, 'r') as f:
            for row in csv.reader(f):
                ws.append(row)
        wb.save("results/excel/" + sample_filename + ".xlsx")