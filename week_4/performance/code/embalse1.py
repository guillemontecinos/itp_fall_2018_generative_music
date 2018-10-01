# Guillermo Montecinos
# Code for Generative Music Performance #1
# ITP Fall 2018

import csv
import midiutil
import numpy
from scipy import stats

# declare input and output file paths
csv_input = '../data/1701embalse.csv'
midi_output = '../midi_folder/embalse1.mid'

# Define a dictionary for embalses to midinotes
notes = {"Cipreses":72,"Rapel":69,"El_Toro":67,"Colbun":64,"Machicura":74,"Canutillar":71,"Pehuenche":62,"Pangue":65,"Ralco":60} # Cmaj scale

max_gen = {"Cipreses":2544,"Rapel":9048,"El_Toro":10800,"Colbun":11376,"Machicura":2280,"Canutillar":4128,"Pehuenche":13680,"Pangue":11208,"Ralco":16560}

# Functions

def save_midi(midi_file):
    filename = midi_output
    with open(filename, 'wb') as output_file:
        midi_file.writeFile(output_file)
        print 'midi file saved'

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
        print time
        if time >= 0:
            column = 1
            while column < len(in_data[i]):
                note = notes[in_data[0][column]]
                volume = int(127*int(in_data[i][column])/int(max_gen[in_data[0][column]]))
                # print("track", track,"channel",channel,"note:",note,"time:",time,"duration:",duration,"volume:",volume)
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
