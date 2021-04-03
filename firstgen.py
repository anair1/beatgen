import midiutil
from midiutil.MidiFile import MIDIFile
import numpy as np

channel = 0
duration = 0.5
tempo = 135
velocity = 100
root_note = 60

my_midi = MIDIFile(numTracks=3)
my_midi.addTempo(0, 0, tempo)

# Hi-hat channel
my_midi.addTrackName(0, 0, 'Hi-hats')
for x in np.arange(0.0, 16.0, 0.5):
    my_midi.addNote(0, channel, root_note, x, duration, velocity)
# Snare channel
my_midi.addTrackName(1, 0, 'Snare')
for x in np.arange(2.0, 16.0, 4.0):
    my_midi.addNote(1, channel, root_note, x, duration, velocity)
# Kick channel
my_midi.addTrackName(2, 0, 'Kick')
for x in np.arange(0.0, 16.0, 8.0):
    my_midi.addNote(2, channel, root_note, x, duration, velocity)
    my_midi.addNote(2, channel, root_note, x + 1.5, duration, velocity)
    my_midi.addNote(2, channel, root_note, x + 4.0, duration, velocity)
    my_midi.addNote(2, channel, root_note, x + 5.0, duration, velocity)
    my_midi.addNote(2, channel, root_note, x + 7.5, duration, velocity)

with open('drums.mid', 'wb') as output_file:
    my_midi.writeFile(output_file)