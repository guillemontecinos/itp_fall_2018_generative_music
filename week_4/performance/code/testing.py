# Guillermo Montecinos
# Code for Generative Music Performance #1
# ITP Fall 2018

import csv
import midiutil
import numpy
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

def note_assign(plant, octave, scale, number_of_notes, data_set):
    # plant: string corresponding to the header of the data_set
    # octave: distance in octaves from central C (Midi: 60)
    # scale: a list with the used scale, centered in central C
    # number_of_notes: range of noted assigned to the data_set
    stats = get_stats(data_set, plant)
    mean = stats['mean']
    stdev = stats['stdev']
    set = []
    set_len = 6/float(number_of_notes)
    for i in range(number_of_notes):
        set.append([stdev * (-3 + i * set_len), stdev * (-3 + (i + 1) * set_len)])
    print len(set)
    

note_assign("Bocamina_II", 20, "major", 10, generation)
