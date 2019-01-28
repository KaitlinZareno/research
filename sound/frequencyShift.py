import soundfile as sf

data, samplerate = sf.read('money track.WAV')
sf.write('money_shift.wav',data, 10000)


# files are currrently too long -- getting a run time error

# money sound at 10 minutes
