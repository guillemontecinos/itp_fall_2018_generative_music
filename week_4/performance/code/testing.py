# Guillermo Montecinos
# Code for Generative Music Performance #1
# ITP Fall 2018

import csv
import midiutil
import numpy
import math
from scipy import stats

csv_input = '../data/embalse_bocamina.csv'

c_maj = [60,62,64,65,67,69,71,72]

with open(csv_input, 'rb') as csvfile:
    data = csv.reader(csvfile)
    generation = []
    for column in data:
        generation.append(column)

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

def note_assign(value, plant, octave, scale, number_of_notes, data_set):
    # plant: string corresponding to the header of the data_set
    # octave: distance in octaves from central C (Midi: 60)
    # scale: a list with the used scale, centered in central C
    # number_of_notes: range of noted assigned to the data_set
    stats = get_stats(data_set, plant)
    mean = stats['mean']
    stdev = stats['stdev']
    # calculates set depending on number of notes and stdev
    set = []
    set_len = 6/float(number_of_notes)
    for i in range(number_of_notes):
        set.append([stdev * (-3 + i * set_len), stdev * (-3 + (i + 1) * set_len)])
    # define set entry corresponding to the mean note
    mean_note = math.trunc(numpy.median(range(number_of_notes)))
    found = 0
    for j in range(len(set)):
        if (set[j][0] <= value and value < set[j][1]):
            found = scale[j - mean_note] + (octave + int(round((j - mean_note) / 8))) * 12
            # add rounded int(round((j - mean_note) / 8)) for cases when we go further to 1 octave
            break
    if found == 0:
        found = scale[0] + octave * 12
    return found


# print note_assign(float(generation[9][9]),"Ralco", 1, c_maj, 4, generation)
# print generation[9][9]
for i in range(1,len(generation)):
    print note_assign(float(generation[i][9]),"Ralco", 1, c_maj, 4, generation)
    # print generation[i][9]

# print("value", "modulo", "division")
# for i in range(30):
#     print(i, i % 12, round(i / 12))
