import random
from desenhojogo import desenhar_forca, mensagem_perdedor, mensagem_vencedor

def jogar():
    # Jogo da forca
    print("********************************")
    print("Bem vindo ao jogo de forca")
    print("********************************")

    # lendo arquivos
    palavras = []

    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    letras_acertadas = ["_"] * len(palavra_secreta)
    total_tentativas = len(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while not enforcou and not acertou and tentativas < total_tentativas:
        chute = input("Digite uma letra? ").strip()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    print("Encontrei a letra {}, na posição {}".format(letra, index))
                    letras_acertadas[index] = letra
        else:
            tentativas += 1

        enforcou = tentativas == total_tentativas
        acertou = "_" not in letras_acertadas
        print("Letras acertadas: {}".format(letras_acertadas))
        print("Tentativas restantes: {}".format(total_tentativas - tentativas))

        if acertou:
            mensagem_vencedor()
        elif enforcou:
            desenhar_forca(tentativas)
            mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")