# Guillermo Montecinos
# Code for Generative Music Performance #1
# ITP Fall 2018

import csv
import midiutil
import numpy
from scipy import stats

csv_input = '../data/1701embalse.csv'

with open(csv_input, 'rb') as csvfile:
    data = csv.reader(csvfile)
    generation = []
    for column in data:
        generation.append(column)

    i = 1
    while i < len(generation):
        time = int(generation[i][0])
        i+=1
        print time
