import os
from random import randint
from midiutil.MidiFile import MIDIFile
import numpy as np

soundfonts_dir = f'{os.path.realpath(__file__)}/soundfonts'
bass_sf = [f for f in os.listdir(f'{soundfonts_dir}/bass') if f.endswith('sf2')]
bass_line = 31
timidity_dir = '/usr/local/Cellar/timidity/2.15.0_1/share/timidity/timidity.cfg'

cfg_file = open(timidity_dir)
cfg_lines = cfg_file.readlines()
cfg_file.close()

bl = cfg_lines[bass_line].split(' ')
bl[4] = f'\"bass/{bass_sf[randint(0, len(bass_sf) - 1)]}\"'
cfg_lines[bass_line] = ' '.join(bl)

cfg_file = open(timidity_dir, 'w')
new_cfg = ''.join(cfg_lines)
cfg_file.write(new_cfg)
cfg_file.close()

def bass_note():
    r = randint(1,7)
    if r % 5 == 0:
        return 27
    elif r % 6 == 0:
        return 23
    elif r % 7 == 0:
        return 31
    return 24

my_midi = MIDIFile(numTracks=1)
my_midi.addTrackName(0, 0, 'Bass')
tempo = 150
my_midi.addTempo(0, 0, tempo)
bass_track = 0
bass_channel = 0
bass_duration = 1.0
velocity = 100
for x in np.arange(0.0, 16.0, 8.0):
    my_midi.addNote(bass_track, bass_channel, bass_note(), x, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_note(), x + 1.5, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_note(), x + 4.0, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_note(), x + 5.0, bass_duration, velocity)
    my_midi.addNote(bass_track, bass_channel, bass_note(), x + 7.5, bass_duration, velocity)

with open('bass.mid', 'wb') as output_file:
    my_midi.writeFile(output_file)