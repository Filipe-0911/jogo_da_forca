def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "banana"
    
    enforcou = False
    acertou = False
    
    while (not enforcou and not acertou):
        chute = input("Qual letra? ").strip()
        index = 0
        
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                print(f"encontrei a letra {letra} na posicao {index}")
                acertou = True
                   
            index = index + 1
            
    
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
