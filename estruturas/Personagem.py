import random
class personagem(object):

    def andar(self):
        print("Você andou um espaço!")

    def voar(self):
        print("Você voou um espaco!")

    def nadar(self):
        print("Você nadou um espaço!")

    def pular(self):
        print("Você pulou sobre um espaço!")

    def virar_direita(self):
        print("Você virou o lado direito")

    def virar_esquerda(self):
        print("Você virou o lado esquerdo")



    def battle(self):
        print ("Um inimigo aparece a sua frente")

    def possibilidade(probability):
        if random.random() < probability:
            battle(self)

    probability = 1,6
    possibilidade(probability)
def main():
    gamestart = personagem()

    while(True):
        menu = int(input("O que deseja fazer? \n"
                         "1) Andar \n"
                         "2) Voar \n"
                         "3) Nadar \n"
                         "4) Pular \n"
                         "5) Virar para direita \n"
                         "6) Virar para esquerda"))

        match(menu):
            case 1: gamestart.andar()
            case 2: gamestart.voar()
            case 3: gamestart.nadar()
            case 4: gamestart.pular()
            case 5: gamestart.virar_direita()
            case 6: gamestart.virar_esquerda()
            case _: print("Isso não é uma ação")

if __name__ == '__main__':
    main()