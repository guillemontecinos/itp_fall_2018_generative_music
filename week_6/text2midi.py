import os
import midiutil

filename = 'radiohead_sim_4_cleaned'
input = []

def save_midi(midi_file, outname):
    # filename = midi_output
    with open(outname, 'wb') as output_file:
        midi_file.writeFile(output_file)
        print 'midi file saved'

def compose_midi(song):
    # setup midifile
    track = 0
    channel = 0
    time = 0   # in beats
    tempo = 120  # beats per minute
    volume = 100 # from 0-127
    midi_file = midiutil.MIDIFile(1, adjust_origin=True)
    midi_file.addTempo(track, time, tempo)
    # compose notes from coded text
    notes = song.split(" ")
    for each_note in notes:
        pitch = int(each_note.split("_")[0])
        if pitch > 255:
            pitch = int(pitch/100)
        duration = float(tempo)*float(each_note.split("_")[1])/60000
        # duration = 1
        if duration != 0.0:
            midi_file.addNote(track, channel, pitch, time, duration, volume)
        time = time + duration
        print("note:", pitch,"time:",duration)
    return midi_file

with open('./simulations/' + filename + '.txt', 'r') as input_file:
    input = input_file.read().split("/")

counter = 1
for song in input:
    midi_file = compose_midi(song)
    save_midi(midi_file,'./output/' + filename + '_' + str(counter) + '.mid')
    counter = counter + 1
    # print song

    # ONLY FOR DEBUGGING
    # notes = song.split(" ")
    # for each_note in notes:
    #     print each_note
