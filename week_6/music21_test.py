from music21 import *

# littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#")
# littleMelody.show()
# littleMelody.show('midi')

# dicant = corpus.parse('trecento/Fava_Dicant_nunc_iudei')
# dicant.plot('histogram', 'pitch')

bwv295 = corpus.parse('bach/bwv295')
for thisNote in bwv295.recurse().notes:
  thisNote.addLyric(thisNote.pitch.german)
bwv295.show()
