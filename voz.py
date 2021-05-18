#code created by me, matthew quirino
from gtts import gTTS
from playsound import playsound
import assunto
import texto
import time 

def play():
    assuntos = assunto.assunto().replace("_", " ")
    #capture the words 
    teste = "Olá, aqui vai um breve resumo sobre %s" %(assuntos)
    
    voz =  gTTS('%s' %(teste), lang='pt', slow=False)
    voz.save('voz.mp3')
    #definitly play the song
    playsound('voz.mp3')
    

def biografia():
    textos = texto.paragrafos()
    print(textos)
    time.sleep(1)
    voz = gTTS('%s' %(textos), lang='pt')
    voz.save('biografia.mp3')
    playsound('biografia.mp3')

play()

biografia()