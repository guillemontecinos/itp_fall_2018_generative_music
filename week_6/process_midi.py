# from Generative Music's Class 2 Code
from mido import MidiFile
file_name = '21_knives_out'
mid = MidiFile('dataset/radiohead/' + file_name + '.mid')

# look at the track names
for i, track in enumerate(mid.tracks):
    print((i, track.name))

# create array of notes
notes = []
messages = []
for message in mid.tracks[7]:
    messages.append(message)

for m in range(len(messages)):
    # print messages[m]
    note = ""
    time = ""
    if messages[m].type == 'note_on':
        message_components = str(messages[m]).split(' ')
        for item in message_components:
            if 'note=' in item:
                # notes.append(item.split('note=')[1])
                note = item.split('note=')[1]
        message_components = str(messages[m+1]).split(' ')
        for item in message_components:
            if 'time=' in item:
                time = item.split('time=')[1]
    if note != "":
        notes.append(str(note + "_" + time))

notes = ' '.join(notes)
# print notes

# write notes to text file
note_file = open('./assets/' + file_name + '.txt', 'w')
note_file.write(notes)
note_file.close()
