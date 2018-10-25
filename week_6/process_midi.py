# from Generative Music's Class 2 Code
from mido import MidiFile
mid = MidiFile('dataset/radiohead/19_idioteque.mid')

# look at the track names
for i, track in enumerate(mid.tracks):
    print((i, track.name))

# create array of notes
notes = []
# for message in mid.tracks[4]:
#     print message
#     note = ""
#     time = ""
#     if message.type == 'note_on':
#         message_components = str(message).split(' ')
#         for item in message_components:
#             if 'note=' in item:
#                 # notes.append(item.split('note=')[1])
#                 note = item.split('note=')[1]
#     elif message.type == 'note_off':
#         message_components = str(message).split(' ')
#         for item in message_components:
#             if 'time=' in item:
#                 # notes.append(item.split('time=')[1])
#                 time = item.split('time=')[1]
#     notes.append(note + "_" + time)
# notes = ' '.join(notes)
#
# # write notes to text file
# note_file = open("./assets/notes.txt", "w")
# note_file.write(notes)
# note_file.close()

messages = []
for message in mid.tracks[4]:
    messages.append(message)
# print messages

for m in range(len(messages)):
    print messages[m]
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
note_file = open("./assets/notes.txt", "w")
note_file.write(notes)
note_file.close()
