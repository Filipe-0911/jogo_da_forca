import os.path
import random

pasta_palavras = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'palavras')
caminho_completo = os.path.join(pasta_palavras, 'palavras.txt')

def jogar():
    mensagem_de_bem_vindo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = cria_lista_palavras(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    
    while not enforcou and not acertou:
        chute = input("Qual letra? ").strip()
        chute = chute.lower()
        index = 0

        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    print(f"encontrei a letra {letra} na posicao {index}")
                    letras_acertadas[index] = letra                   
                index += 1
        else:
            erros += 1
            if erros < len(palavra_secreta):
                print(f"Você ainda tem {len(palavra_secreta) - erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
        print("Fim do jogo")
    if enforcou:
        print("Você perdeu!")
        print("Fim do jogo")


def mensagem_de_bem_vindo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    palavras = []

    with open(caminho_completo) as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    
    indice = random.randrange(0, len(palavras))

    palavra_secreta = palavras[indice].lower()

    return palavra_secreta

def cria_lista_palavras(palavra):
    lista_palavras = ["_" for letras in palavra]
    return lista_palavras

if(__name__ == "__main__"):
    jogar()