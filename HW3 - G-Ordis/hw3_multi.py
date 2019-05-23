import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import pysal
import multiprocessing as mp
import collections

import csv
import pickle

word_list = set()
word_dict = collections.defaultdict(dict)

# Region to word
with open('subdivision_to_word_counts.tsv', 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for line in reader:
        id_ = line[0]
        list_of_val = line[1].split()
        for a in range(int(len(list_of_val)/2)):
            loc_id = list_of_val[a*2]
            value = int(list_of_val[a*2+1])
            word_dict[id_][loc_id] = value
            word_list.add(loc_id)

word_list = sorted(word_list, reverse=False)

word_vec = {}

for key, value in word_dict.items():
    word_vec[key] = [value.get(word, 0) for word in word_list]
    
region2word = pd.DataFrame.from_dict(word_vec, columns=word_list, orient='index')
print('Loaded words')

# Region to neighbor
region_set = set()
region_dict = {}

with open('subdivision-to-neighbors.tsv', 'r') as file:
    reader2 = csv.reader(file, delimiter='\t')
    i=0
    for line in reader2:
        id_ = line[0]
        adj = [x for x in line[1].split()]
        region_set |= set(adj)
        
        region_dict[id_] = adj

not_in_wordcounts = set(region_set).difference(set(region2word.index.values))
not_in_wordcounts = {x:list(np.zeros(len(region2word.columns))) for x in not_in_wordcounts}

df2 = pd.DataFrame.from_dict(not_in_wordcounts, columns=word_list, orient='index')
region2word_full = region2word.append(df2)
region2word_full = region2word_full.sort_index()

conv_dict = {}
for word in region2word_full.columns:
    conv_dict[word] = list(region2word_full[word])

weight_binary = pysal.W(region_dict, id_order=region2word_full.index.values)
print('Loaded neighbors')

file = open('getis_result.csv', 'w')
writer = csv.writer(file, delimiter='\t')

def get_g(word):
    print(word)
    test = pysal.G_Local(conv_dict[word], weight_binary, permutations=99)
    Zval = test.Zs
    Zsimval = test.z_sim

    return (word, Zval, Zsimval)

print('Function defined')

def main():                              
    mp.freeze_support()

    workers = mp.cpu_count() - 3
    pool = mp.Pool(processes=workers)
    input_mp = list(conv_dict.keys())

    results = pool.map(get_g, input_mp)

    with open('getis_result.csv', 'w') as file:
        writer = csv.writer(file, delimiter='\t')
        for tup in results:
            writer.writerows([tup[0], tup[1], tup[2]])

# Multiprocessing portion    
if __name__ == '__main__':
    main()