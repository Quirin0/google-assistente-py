import time
import requests
from bs4 import BeautifulSoup
import keyboard


#funcao main é onde tudo se inicia :)
#funcao acesso é o acesso ao site e requisicao dos dados

print('Sobre qual assunto você deseja pesquisar?')
pesquisa = input().replace(" ", "_") 

def assunto():    
    pesquisas = pesquisa
    return pesquisas


def acesso():
    pesquisa = assunto()

    #faz a requisicao de acesso ao site e adiciona oque a pessoa deseja pesquisar na URL
    req = requests.get('https://pt.wikipedia.org/wiki/%s' %(pesquisa))

    #verifica se o site permitiu o acesso
    if req.status_code == 200:
        print('Requisição bem sucedida!')
        print('Pesquisando...')
        content = req.content
        return content
        
    #caso nao tenha conseguido acesso ao site isso aparecerá    
    else:
        print('Não foi possivel fazer a pesquisa... Tente novamente')
        
        


'''
def main():
    x = acesso()
    print(x)


if __name__ == "__main__":
    main()'''