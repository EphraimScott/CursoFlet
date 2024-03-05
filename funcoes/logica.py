#Logica  com estruturas

"""

 FIXME:estrutura de seleção B.O. logico

  Aqui use os operadores logicos e relacionais

 FIXME:estrutura de repetição B.O. de repetição

 Aqui use todos os operadores, variaveis contadoras e acumuladoras

 FIXME:estrutura de dados B.O. de dados

 Aqui use vetores, matrizes, listas, duplas e dicionarios
 Organizam e armazenam dados de arquivos externos e bancoos de dados

"""

#Criar uma função que varifique se o numero é positivo, negatico ou nulo

def verifica_numero(num):

    if num > 0:
        print("Positivo")
    elif num < 0:
        print("Negativo")
    else:
        print("Nulo")

def paridade(num):
    modular = num % 2

    if modular == 0:
        print("Esse numero é par")
    else:
        print("Esse numero é impar")

def escrever_nome(nome):
    for letra in nome:
        print(letra,end='')
        time.sleep(0.2)