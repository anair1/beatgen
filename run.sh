echo "Generating a beat...Drums..."
python drumgen.py
timidity drums.mid -Ow -o drums.wav
echo "Done. Bass..."
python bassgen.py
timidity bass.mid -Ow -o bass.wav
echo "Done. Combining..."
python wavmix.py
mv output.wav bin
echo "Done. Output file is in bin directory."
rm drums.* bass.*