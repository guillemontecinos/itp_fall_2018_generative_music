from mido import MidiFile
mid = MidiFile('twinkle_twinkle.mid')
# mid = MidiFile('../jara_manifiesto.mid')

# look at the track names
for i, track in enumerate(mid.tracks):
    print((i, track.name))

# create array of notes
notes = []
for message in mid.tracks[1]:
    # print message
    if message.type == 'note_on':
        message_components = str(message).split(' ')
        for item in message_components:
            if 'note=' in item:
                notes.append(item.split('note=')[1])
print 'min: ' + min(notes)
print 'max: ' + max(notes)
notes = ' '.join(notes)

# write notes to text file
note_file = open("../markov_code/assets/notes.txt", "w")
note_file.write(notes)
note_file.close()
