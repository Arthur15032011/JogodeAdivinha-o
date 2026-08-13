import random
from desenhojogo import desenhar_forca, mensagem_perdedor, mensagem_vencedor

#Jogo da forca
print("********************************")
print("Bem vindo ao jogo de forca")
print("********************************")

# lendo arquivos
with open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())


numero = random.randrange(0, len(palavras))

palavrasecreta = palavras[numero]

letras_acertadas = ["_"]*len(palavra_secreta)
total_tentativas = len(palavra_secreta)

print(letras_acertadas)

enforcou = False
acertou = False
tentativas = 0

while(not enforcou and not acertou and tentativas > 5):
    chute = input("Digite uma letra? ")
    chute = chute.strip()

    if(chute in palavra_secreta):
      index = 0
      for letra in palavra_secreta:
        if(chute == letra):
            print("Encontrei a letra {}, letra, na posição {}". format(letra, index))
            letras_acertadas[index] = letra
        index = index + 1
    else:
        tentativas = tentativas + 1

    #controle de tentavas
    enforcou = tentativas == total_tentativas
    acertou = "_" not in letras_acertadas
    print("Letras acertadas: {}".format(letras_acertadas))
    print("Tentativas restantes: {}".format(total_tentativas - tentativas))

    if(acertou):
        mensagem_vencedor()
    elif(enforcou):
        desenhar_forca(tentativas)
        mensagem_perdedor(palavra_secreta)

print("Fim do jogo")