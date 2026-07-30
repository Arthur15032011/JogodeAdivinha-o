#Jogo da forca
print("********************************")
print("Bem vindo ao jogo de forca")
print("********************************")

palavra_secreta = "forte"
letras_acertadas = ["_","_","_","_","_","_"]

enforcou = False
acertou = False

while(not enforcou and not acertou):
    chute = input("Digite uma letra? ")
    chute = chute.strip()
    
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            print("Encontrei a letra {}, letra, na posição {}". format(letra, index))
            index = index + 1
            

    print("jogando")

print("Fim do jogo")