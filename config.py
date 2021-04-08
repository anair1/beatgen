from random import randint
from os import listdir

timidity_dir = '/usr/local/Cellar/timidity/2.15.0_1/share/timidity/timidity.cfg'
soundfonts_dir = "/Users/arjunnair/Documents/Github/soundfonts"
drums_lines = {'hihatcl':54,
               'hihatop':58,
               'snare1':51,
               'snare2':52,
               'kick1':48,
               'kick2':49}
bass_line = 31
drums_sf = [f for f in listdir(f'{soundfonts_dir}/drums') if f.endswith('sf2')]
bass_sf = [f for f in listdir(f'{soundfonts_dir}/bass') if f.endswith('sf2')]

cfg_file = open(timidity_dir)
cfg_lines = cfg_file.readlines()
cfg_file.close()

for d, l in drums_lines.items():
    line = cfg_lines[l].split(' ')
    line[4] = f'\"drums/{drums_sf[randint(0, len(drums_sf) - 1)]}\"'
    cfg_lines[l] = ' '.join(line)

bl = cfg_lines[bass_line].split(' ')
bl[4] = f'\"bass/{bass_sf[randint(0, len(bass_sf) - 1)]}\"'
cfg_lines[bass_line] = ' '.join(bl)

cfg_file = open(timidity_dir, 'w')
new_cfg = ''.join(cfg_lines)
cfg_file.write(new_cfg)
cfg_file.close()
