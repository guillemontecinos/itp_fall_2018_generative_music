# Guillermo Montecinos
# Code for Generative Music Performance #1
# ITP Fall 2018

import csv
import midiutil
import numpy
from scipy import stats

# declare input and output file paths
csv_input = '../data/embalse_bocamina.csv'
midi_output = '../midi_folder/embalse_bocamina.mid'

# Define a dictionary for embalses to midinotes
notes = {"Cipreses":72,"Rapel":69,"El_Toro":67,"Colbun":64,"Machicura":74,"Canutillar":71,"Pehuenche":62,"Pangue":65,"Ralco":60} # Cmaj scale

max_gen = {"Cipreses":2544,"Rapel":9048,"El_Toro":10800,"Colbun":11376,"Machicura":2280,"Canutillar":4128,"Pehuenche":13680,"Pangue":11208,"Ralco":16560,"Bocamina_II":8400}

# Functions
# midi fave function
def save_midi(midi_file):
    filename = midi_output
    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)
        print 'midi file saved'

# get stats function
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

# note assgin function

# midi composer function
def compose_midi(in_data,notes,max_gen):
    track = 0
    channel = 0
    time = 0 # in beats
    tempo = 60  # beats per minute
    # volume = 100 # from 0-127
    program = 0 # Midi instrument

    midi_file = midiutil.MIDIFile(1, deinterleave=False, adjust_origin=False)
    midi_file.addTempo(track, time, tempo)
    # midi_file.addProgramChange(track, channel, time, program)
    duration = 1.0
    i = 1
    while i < len(in_data):
        time = float(in_data[i][0])
        # print time
        if time >= 0:
            column = 1
            while column < len(in_data[i]):
                # if column is ralco do notes to trigger mapuche samples
                    # call assign_note. the scale doesn't matter cause it will trigger samples, but the amount of notes is important because it depends on the number of samples triggered.
                if in_data[0][column] == "Ralco":
                    print "Ralco!"
                # elseif column is bocamina create bass
                    # function assign_note depending on number of notes desired, octave desired. It may assign the media of the data to the root of the octave desired. So, the range of notes should be +/-1 octave from the choosen octave.
                elif in_data[0][column] == "Bocamina_II":
                    print "Bocamina_II!"
                # else do chords
                else:
                    note = notes[in_data[0][column]]
                    volume = int(127*int(in_data[i][column])/int(max_gen[in_data[0][column]]))
                    midi_file.addNote(track, channel, note, time, duration, volume)
                column += 1
            i += 1
    save_midi(midi_file)

# main algorythm
with open(csv_input, 'rb') as csvfile:
    data = csv.reader(csvfile)
    generation = []
    for column in data:
        generation.append(column)
    # print embalse[generation[0][-1]]
    # process data
    compose_midi(generation,notes,max_gen)
