#FIXME: O que é uma classe?

"""
uva, morango, macã, laranja
A (Curte Whatsapp) B (Curte rede social) C (Não curte nada)
"""

class DemoEstrutura(object):
    def __init__(self):
        pass

    def mostrar_for(self):
        for _ in range(10):
            print("Eu estou tentando codar! ;-;")

    def mostrar_while(self):
        pass
    def mostrar_alo(self):
        print("Yo POO!")

def main():
    demo1 = DemoEstrutura()

    while(True):
     menu = int(input("Escolha a opção do menu: \n "
                      "1) Mostrar Alô POO \n "
                      "2) Mostrar a repetição \n "
                      "9) Sair"))

     match(menu):
       case 1: demo1.mostrar_alo()
       case 2: demo1.mostrar_for()
       case 9: break
       case _: print("Não é uma opção")

if __name__ == '__main__':
    main()