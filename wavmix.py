from pydub import AudioSegment

dir = "/Users/arjunnair/Documents/Github/beatgen"
drums = AudioSegment.from_file(f'{dir}/drums.wav')
bass = AudioSegment.from_file(f'{dir}/bass.wav')
combined = drums.overlay(bass)

combined.export(f'{dir}/output.wav', format='wav')