#Jogo da Forca simples usando listas, while e for loop em Python

import random #Módulo para randomizar escolhas das palavras no jogo

#Cada lista corresponde a um tema
#1-animais
#2-países
#3-objetos
listaPalavras = [["peixe","baleia","polvo"],["madagascar","brasil","argentina"],["pedra","papel","tesoura"]]

#Loop do jogo

while True:
    print("Jogo da Forca\n")
    print("Escolha uma opção: 1-Animais| 2-Países| 3-Objetos| 4- Sair do jogo")
    entrada = input("Digite um número: ")

    #Condicionais para a escolha do usuário

    if entrada == "4":
        break #finaliza o loop
    elif entrada== "1":
        palavra = random.choice(listaPalavras[0])#seleciona aleatoriamente uma palavra da primeira lista

    elif entrada== "2":
        palavra = random.choice(listaPalavras[1])#seleciona aleatoriamente uma palavra da segunda lista

    elif entrada== "3":
        palavra = random.choice(listaPalavras[2])#seleciona aleatoriamente uma palavra da terceira lista

    forca = ["-"] * len(palavra) #cria uma lista com "-" para cada letra da palavra

    letras_erradas = []#lista vazia para armazenar letras erradas digitadas pelo usuário
    
    #Antes do loop do jogo vamos adicionar um print informando o tamanho da palavra escolhida
    print("A palavra tem " + str(len(palavra)) + " letras.")

    
    for i in range(10): #o range vai ser igual a quantidade de chances que o jogador terá para completar a palavra

        jogada = input("Digite uma letra: ").lower() #transforma a letra em minúsculo
        #Condicionais para a letra escolhida pelo jogador

        if jogada in palavra: #verifica se a letra escolhida está na palavra selecionada
            for j in range(len(palavra)):
                if palavra[j] == jogada:
                    forca[j] = jogada #substitui o "-" na posição [j] pela letra escolhida na lista forca

            resposta = "".join(forca)#transforma a lista forca em uma string
            print("Ok! Letra contida, forca: " + resposta)

            if resposta == palavra:
                print("Parabéns, você acertou a palavra é " + resposta + "!")
                break #finaliza a rodada pois o usuário completou a palavra

        else: #caso a letra digitada pelo jogador não esteja na palavra escolhida
            letras_erradas +=[jogada] #adiciona a letra errada na lista de letras erradas
            letrasErradas = "".join(letras_erradas)#transformamos a lista em string para que possâmos adicionar na frase
            resposta = "".join(forca)
            #Mostra para o usuário as letras não contidas que ele já usou
            print("A letra escolhida não está contida na plavra.\n" + resposta+"\n Letras não contidas: " + letrasErradas)

    else:#Se o usuário já jogou 10 vezes e ainda não acertou a palavra
        print("Você perdeu! Forca!")





        





    
         
         




















    
        






