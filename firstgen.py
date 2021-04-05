import midiutil
from midiutil.MidiFile import MIDIFile
import numpy as np

channel = 9
duration = 0.5
tempo = 135
velocity = 100
root_note = 60

my_midi = MIDIFile(numTracks=4)
my_midi.addTempo(0, 0, tempo)

# Hi-hat track
my_midi.addTrackName(0, 0, 'Hi-hats')
hat_track = 0
hat_note = 42
for x in np.arange(0.0, 16.0, 0.5):
    my_midi.addNote(hat_track, channel, hat_note, x, duration, velocity)

# Snare track
my_midi.addTrackName(1, 0, 'Snare')
snare_track = 1
snare_note = 40
for x in np.arange(2.0, 16.0, 4.0):
    my_midi.addNote(snare_track, channel, snare_note, x, duration, velocity)

# Kick track
my_midi.addTrackName(2, 0, 'Kick')
kick_track = 2
kick_note = 35
for x in np.arange(0.0, 16.0, 8.0):
    my_midi.addNote(kick_track, channel, kick_note, x, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 1.5, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 4.0, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 5.0, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 7.5, duration, velocity)

# Bass Track
my_midi.addTrackName(2, 0, 'Bass')
bass_track = 0
bass_channel = 15
bass_notes = {'c0': 12, 'd#0': 15, 'g0': 19, 'b0': 23, 'c1': 24, 'd#1': 27, 'g1': 31}
bass_duration = 1.0
for x in np.arange(0.0, 16.0, 8.0):
    my_midi.addNote(bass_track, bass_channel, bass_notes['d#1'], x, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_notes['c1'], x + 1.5, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_notes['g1'], x + 4.0, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_notes['c1'], x + 5.0, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_notes['b0'], x + 7.5, bass_duration, velocity)

with open('drums.mid', 'wb') as output_file:
    my_midi.writeFile(output_file)