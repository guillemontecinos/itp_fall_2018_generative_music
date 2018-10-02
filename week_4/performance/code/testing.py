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
    # column = 0
    # while column < len(generation[0]):
        # print generation[0][column]
        # if generation[0][column] == "Bocamina_II":
        #     print "Bocamina!"
        # else:
        #     print "Not Bocamina :()"
        # column = column + 1

    # print generation[0]

    # i = 1
    # while i < len(generation):
    #     time = int(generation[i][0])
    #     i+=1
    #     print time

def get_stats(data, header):
    # based on ufo_by_date.py get_stats function
    data_list = []
    column = 0
    # search for header
    i = 0
    while i < len(data[0]):
        if data[0][i] == header:
            column = i
        i = i + 1
    if column == 0:
        print "Entry was not found in data set."
        return
    # extract dat from column
    row = 1
    while row < len(data):
        data_list.append(float(data[row][column]))
        row = row + 1
    stdev = numpy.std(data_list)
    mean = numpy.mean(data_list)
    median = numpy.median(data_list)
    mode = stats.mode(data_list)
    return {
        "mean": mean,
        "median": median,
        "mode": mode[0],
        "stdev": stdev
    }

def note_assign(plant, central_note, scale, number_of_notes, data_set):
    stats = get_stats(data_set, plant)
    mean = stats['mean']
    stdev = stats['stdev']
    set = []
    set_len = 6/number_of_notes
    i = 0
    while i < number_of_notes:
        # set[i] = [- 3 * stats['stdev'] + i * set_len * stats['stdev'], - 3 * stats['stdev'] + (i + 1) * set_len * stats['stdev']]
        set[i] = [stdev * (-3 + i * l), stdev * (-3 + (i + 1) * l)]
        i = i + 1
    print set
    # each sets entry corresponds to one note, and each entry will have a list that will define each range
    if scale == "major":
        # for energy in data_set:
        print "Scale is major"

    else:
        print "Scale is not major"
        # break


number_of_notes = 10
stats = get_stats(generation, 'Bocamina_II')
mean = stats['mean']
stdev = stats['stdev']
set = []
set_len = 6/float(number_of_notes)
# print set_len
# print stdev
for i in range(number_of_notes):
    set.append([stdev * (-3 + i * set_len), stdev * (-3 + (i + 1) * set_len)])
print set
