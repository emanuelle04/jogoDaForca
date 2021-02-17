#Criando Jogo da Forca com conceitos básicos de Python :)

import random #Importa a biblioteca que usaremos para randomizar a escolha das palavras no jogo

dicionarioTemas = { #Criamos um dicionário com três temas, cada um com quatro palavras para as partidas.
  "cores":["magenta", "ciano", "esmeralda", "chumbo"],
  "frutas":["acerola", "goiaba", "graviola", "abacate"],
  "estados":["pernambuco", "alagoas", "acre", "tocantins"]
}

#Início do loop do Jogo da Forca
while True:
  print("Jogo da Forca\nTemas: 1-Cores | 2-Frutas | 3-Estados | 4- Sair do Jogo")
  entrada = str(input("Digite uma opção: "))
  #Condicionais para a entrada do jogador

  if entrada == "4":
    print("Você saiu do jogo :(")
    break # Termina o loop e finaliza o jogo
  elif entrada == "1":
    palavra = random.choice(dicionarioTemas["cores"])#Seleciona uma palavra aleatória da lista "cores"
  elif entrada == "2":
    palavra = random.choice(dicionarioTemas["frutas"])#Seleciona uma palavra aleatória da lista "frutas"
  elif entrada == "3":
    palavra = random.choice(dicionarioTemas["estados"])#Seleciona uma palavra aleatória da lista "estados"
  
  tentativas = ["-"]*len(palavra) # Aqui criamos uma lista preenchida com "-" um para cada letra da palavra selecionada.
  letrasErradas = [] #Lista vazia que armazenará letras digitadas pelo jogador que não estão na palavra.
  print("Vamos começar, sua palavra tem  " + str(len(palavra)) + " letras.\n")#Mostra para o jogador o número de letras presentes na palavra selecionada

  for i in range(18):
    #O range será igual ao número de chances que o jogador terá para completar a palavra.
    print("".join(tentativas))#Mostra para o jogador a estrutura da palavra
    jogada = str(input("Digite uma letra: "))
    #Verifica se a letra digitada consta na palavra selecionada
    if jogada in palavra: 
      #Se a letra escolhida consta na palavra então é feita a substituição na lista tentativas pela letra na mesma posição da palavra
      for j in range(len(palavra)):
        if palavra[j] == jogada:
          tentativas[j] = jogada
      resposta = "".join(tentativas)
      
      print("Forca: " + resposta + " Chances restantes: " + str(17 - i)) #Aqui mostramos o progresso do jogador e quantas rodadas faltam para o fim da partida

      if resposta == palavra: 
        print("Parabéns, você acertou a palavra é " + resposta + "!")
        break #Finaliza o for loop pois o jogador ganhou

    else:
      letrasErradas +=[jogada] #Caso a letra escolhida pelo jogadpr na conste na palavra ele é adicionada a lista "letrasErradas"
      resposta = "".join(tentativas)
      print("Forca: " + resposta + " Chances restantes: " + str(17-i)) #Aqui mostramos o progresso do jogador e quantas rodadas faltam para o fim da partida
      letrasJaUsadas = " ".join(letrasErradas)
      print("A letra " + jogada + " não está na palavra\n Letras erradas já digitadas: " + letrasJaUsadas) #Avisa ao jogador que a letra digitada está errada e mostra quais letras erradas ele já usou

  else: 
    print("Você perdeu! Forca!") #Caso depois das 18 chances o jogador não tiver concluido e o for loop não for finalizado ele recebe o aviso de que perdeu o jogo.



     











 
  
  









