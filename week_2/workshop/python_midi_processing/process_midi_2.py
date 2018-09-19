from mido import MidiFile
# mid = MidiFile('twinkle_twinkle.mid')
mid = MidiFile('../jara_manifiesto.mid')

# look at the track names and print them
# for i, track in enumerate(mid.tracks):
#     print((i, track.name))

# create array of notes
# notes = []
# time_array = []
# midi_out = []
for message in mid.tracks[4]:
    # print message
    if message.type == 'note_on':
        # print message
        # time_array.append(str(message.time))
        message_components = str(message).split(' ')
        # print message_components
        for item in message_components:
            notes = ''
            times = ''
            if 'note=' in item:
                # notes.append(item.split('note=')[1])
                notes = item.split('note=')[1]
                # print item.split('note=')[1]
            if 'time=' in item:
                # time_array.append(item.split('time=')[1])
                times = item.split('time=')[1]
                # print item.split('time=')[1]
            print (str(notes) + ', ' + str(times))
            # midi_out.append([notes,times]);
# notes = ' '.join(notes)
# time_array = ' '.join(time_array)
#
# # write notes to text file
# # note_file = open("../markov_code/assets/notes.txt", "w")
# note_file = open("../markov_code/assets/notes_sayen.txt", "w")
# note_file.write(notes)
# note_file.close()

# print 'time array: ' + str(len(time_array))
# print 'notes array: ' + str(len(notes))
# print notes
# print time_array
# print midi_out
