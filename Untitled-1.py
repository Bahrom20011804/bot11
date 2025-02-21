import piper

text = "Salom, bu test ovozi."
voice = "en_US-libritts-high"  # O'zbek tili uchun mos ovoz bo'lishi kerak

tts = piper.TTS(voice)
audio = tts.synthesize(text)

with open("output.wav", "wb") as f:
    f.write(audio)
