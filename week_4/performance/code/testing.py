# Guillermo Montecinos
# Code for Generative Music Performance #1
# ITP Fall 2018

import csv
import midiutil
import numpy
from scipy import stats

csv_input = '../data/embalse_bocamina.csv'

with open(csv_input, 'rb') as csvfile:
    data = csv.reader(csvfile)
    generation = []
    for column in data:
        generation.append(column)

    # for column in generation[0]:
    column = 0
    while column < len(generation[0]):
        # print generation[0][column]
        if generation[0][column] == "Bocamina_II":
            print "Bocamina!"
        else:
            print "Not Bocamina :()"
        column = column + 1

    # print generation[0]

    # i = 1
    # while i < len(generation):
    #     time = int(generation[i][0])
    #     i+=1
    #     print time
