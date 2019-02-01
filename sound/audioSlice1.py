import soundfile as sf

data, samplerate = sf.read('money track.WAV')
singleSample = (samplerate*60)-1


for i in range(30):
    l = []
    l = data[i*(singleSample+1):(i+1)*singleSample]
    sf.write('mtCut%d.wav' %i,l,samplerate)

# was able to get the audio slicing code working in ipython but I get a memory error in a python file.

#slice numpy array using for loop
#write script that makes a matplotlib figure that's divided into two figures -- one above other
# bottom is spectogram
# top is graph realpython.com -- 3 graphs on house -- burst of color???
