import jogodaforca
import jogodeadivinhacão as jogodeadivinhacão
def escolherjogo():

    print("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▌")
    print("───▄▄██▌█░░░░MENU░░░░▌.")
    print("▄▄▄▌▐██▌█░░░░ DE ░░░░▌.")
    print("███████▌█▄▄▄▄JOGO▄▄▄▄▄▄▄▌")
    print("▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀")
    print("Escolha o jogo que deseja jogar:")
    print("1 - Jogo da Forca")
    print("2 - Jogo de Adivinhação")
    print("3 - Sair")


jogo = int(input("Digite o número do jogo que deseja jogar: "))
match jogo:
    case 1:
        jogodaforca.jogar()
    case 2:
        jogodeadivinhacão.jogar()
    case 3:
        print("Sair")
        exit()

if __name__ == "__main__":
    escolherjogo()