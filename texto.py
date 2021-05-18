import time
import requests
from bs4 import BeautifulSoup
import keyboard
import assunto
import sys
import codecs
import io
import string

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), sys.stdout.encoding, 'replace')
print(sys.stdout.encoding)
def obterDados():
    content = assunto.acesso()
    
    #organiza os dados do site de maneira estruturada
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def paragrafos():
    soup = obterDados()
    ## finding all p tags
    p_tags = soup.find_all("p")     

        
    print("\n-----Content Of All Paragraphs-----\n")

    for tag in p_tags:
        #print(tag.text)
        
        textos = tag.text.replace("[2][3][4][5][6][7][8][9][10]", " ")
        
        print(textos)
        return textos


'''def main():
    paragrafos()
def criarArquivo():
    textos = paragrafos()
    arquivo = open('arquivo.txt', 'w', encoding="utf-8")
    arquivo.close()

criarArquivo()

if __name__ == '__main__':
    main()'''
paragrafos()