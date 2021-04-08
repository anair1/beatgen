from midiutil.MidiFile import MIDIFile
import numpy as np
from random import randint
import os

timidity_dir = '/usr/local/Cellar/timidity/2.15.0_1/share/timidity/timidity.cfg'
soundfonts_dir = f'{os.path.realpath(__file__)}/soundfonts'
drums_lines = {'hihatop':58,
               'snare1':51,
               'snare2':52,
               'kick1':48,
               'kick2':49}
# bass_line = 31
hihatcl_line = 31
hihatcl_sf = [f for f in os.listdir(f'{soundfonts_dir}/hihatcl') if f.endswith('sf2')]
drums_sf = [f for f in os.listdir(f'{soundfonts_dir}/drums') if f.endswith('sf2')]
# bass_sf = [f for f in listdir(f'{soundfonts_dir}/bass') if f.endswith('sf2')]

cfg_file = open(timidity_dir)
cfg_lines = cfg_file.readlines()
cfg_file.close()

for d, l in drums_lines.items():
    line = cfg_lines[l].split(' ')
    line[4] = f'\"drums/{drums_sf[randint(0, len(drums_sf) - 1)]}\"'
    cfg_lines[l] = ' '.join(line)

hl = cfg_lines[hihatcl_line].split(' ')
hl[4] = f'\"hihatcl/{hihatcl_sf[randint(0, len(hihatcl_sf) - 1)]}\"'
cfg_lines[hihatcl_line] = ' '.join(hl)

cfg_file = open(timidity_dir, 'w')
new_cfg = ''.join(cfg_lines)
cfg_file.write(new_cfg)
cfg_file.close()

channel = 9
duration = 0.5
tempo = 150
velocity = 100
root_note = 60

my_midi = MIDIFile(numTracks=5)
my_midi.addTempo(0, 0, tempo)

# Closed hat track
my_midi.addTrackName(0, 0, 'Closed hat')
hat_track = 0
for x in np.arange(0.0, 16.0, 0.5):
    my_midi.addNote(hat_track, 0, root_note, x, duration, velocity)

# Snare track
my_midi.addTrackName(1, 0, 'Snare')
snare1_track = 1
snare1_note = 40
if randint(1, 4) % 4 == 0:
    snare2_track = 4
    snare2_note = 38
    for x in np.arange(3.5, 16.0, 8.0):
        my_midi.addNote(snare2_track, channel, snare2_note, x, duration, velocity)
        my_midi.addNote(snare2_track, channel, snare2_note, x + 1.0, duration, velocity)
        my_midi.addNote(snare2_track, channel, snare2_note, x + 2.0, duration, velocity)
for x in np.arange(2.0, 16.0, 4.0):
    my_midi.addNote(snare1_track, channel, snare1_note, x, duration, velocity)

# Kick track
my_midi.addTrackName(2, 0, 'Kick')
kick_track = 2
kick_note = 36
for x in np.arange(0.0, 16.0, 8.0):
    my_midi.addNote(kick_track, channel, kick_note, x, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 1.5, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 4.0, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 5.0, duration, velocity)
    my_midi.addNote(kick_track, channel, kick_note, x + 7.5, duration, velocity)

# Open hat track
my_midi.addTrackName(3, 0, 'Open hat')
oh_track = 3
oh_note = 46
for x in np.arange(1.5, 16.0, 4.0):
    my_midi.addNote(oh_track, channel, oh_note, x, duration, velocity)

with open('drums.mid', 'wb') as output_file:
    my_midi.writeFile(output_file)