import speech_recognition as sr

# - criar um "reconhecedor"
rec = sr.Recognizer()

# para escolher qual microfone vamos usar, rode:
# print(sr.Microphone().list_microphone_names())
# - ouvir o audio do microfone
with sr.Microphone() as microfone:
     rec.adjust_for_ambient_noise(microfone)
     print("Pode começar a Falar: ")

     # rec.pause_threshold = 5 -> coloque isso se voce quiser que ele demore para parar de captar seu audio
try:
     audio = rec.listen(microfone)
     # reconhce esse audio e traduz ele pra texto
     texto = rec.recognize_google(audio, language='pt-BR')
     print(texto)
except:
     print("Não Peguei Áudio Nenhum")