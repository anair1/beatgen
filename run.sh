echo "Generating a beat...Drums..."
python3 drumgen.py
timidity drums.mid -Ow -o drums.wav
echo "Done. Bass..."
python3 bassgen.py
timidity bass.mid -Ow -o bass.wav
echo "Done. Combining..."
python3 wavmix.py
mv output.wav bin
echo "Done. Output file is in bin directory."
rm drums.* bass.*