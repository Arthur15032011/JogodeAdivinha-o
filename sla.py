import random
print("********************************")
print("Bem vindo ao jogo de Adivinhação")
print("********************************")

numerosecreto = random.randrange(1, 51)
totaldetentativas = 10


while(totaldetentativas > 0):
    print("Você tem ", totaldetentativas, " tentativas")  

    chute = input("Digite o seu número: ")
    print("Você digitou: ", chute )

    chuteNumerico = int(chute)

    if(totaldetentativas == 0):
        print("Você não tem mais tentativas. Fim do jogo.")
        break

    acertou = chuteNumerico == numerosecreto
    maior = chuteNumerico > numerosecreto
    menor = chuteNumerico < numerosecreto

    # se voce digitar qualquer numero vou verificar se acertou ou errou
    if acertou:
        print("Parabéns! Você acertou! Fim do jogo")
        break

    else:
        if maior:
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor que o número secreto.")

    totaldetentativas = totaldetentativas - 1
print("Fim do jogo")