# from Generative Music's Class 2 Code
# by Guillermo Montecinos
# Oct, 2018
from mido import MidiFile
file_name = '1_there_there'
mid = MidiFile('dataset/radiohead/midi/' + file_name + '.mid')
tpb = mid.ticks_per_beat
print tpb


# look at the track names
for i, track in enumerate(mid.tracks):
    print((i, track.name))

# create array of notes
notes = []
messages = []
for message in mid.tracks[6]:
    if not message.is_meta and message.type != 'control_change' and int(message.time) != 0:
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
    # print time
