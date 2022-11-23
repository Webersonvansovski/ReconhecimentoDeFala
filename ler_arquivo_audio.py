import speech_recognition as sr

rec = sr.Recognizer()

with sr.AudioFile("audio.mav") as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)