import os.path
import random

def jogar():
    mensagem_de_bem_vindo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = cria_lista_palavras(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    
    while not enforcou and not acertou:
        chute = chute_jogador()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            if erros < len(palavra_secreta):
                print(f"Você ainda tem {len(palavra_secreta) - erros} tentativas.")

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        imprime_letra_acertada(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    if enforcou:
        print(f"Você perdeu! A palavra era {palavra_secreta}.")

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra       
        index += 1

def imprime_letra_acertada(palavra_acertada):
    palavra = palavra_acertada
    print(palavra)

def chute_jogador():
    chute = input("Qual letra? ").strip()
    chute = chute.lower()

    return chute

def mensagem_de_bem_vindo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta(nome_arquivo="palavras.txt", inicio_contagem=0):
    pasta_palavras = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'palavras')
    caminho_completo = os.path.join(pasta_palavras, nome_arquivo)
    palavras = []

    with open(caminho_completo) as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    
    indice = random.randrange(inicio_contagem, len(palavras))

    palavra_secreta = palavras[indice].lower()

    return palavra_secreta

def cria_lista_palavras(palavra):
    lista_palavras = ["_" for letras in palavra]
    return lista_palavras

if(__name__ == "__main__"):
    jogar()