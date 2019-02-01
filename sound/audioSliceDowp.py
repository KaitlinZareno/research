import soundfile as sf

data, samplerate = sf.read('dowp.wav')
count = 0
for i in range(14):
    l = []
    for c in range(samplerate):
        l.append(data[(i+1)*c])
        #print(l)
    
    sf.write('dowpCut%d.wav' % count,l, samplerate)
    #print(l)
    count +=1
    del(l)



#slice numpy array using for loop
#write script that makes a matplotlib figure that's divided into two figures -- one above other
# bottom is spectogram
# top is graph realpython.com -- 3 graphs on house -- burst of color???
