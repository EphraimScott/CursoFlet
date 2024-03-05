#Operações Aritimetica

'''
 Basica:

 adição ---> +
 subtração ---> -
 multiplicacao ---> *
 divisao ---> /

 outras

 Divisao inteira ---> //
 Resto da divisao ---> %
 Exponenciação ---> **
'''

#Crie uma função para somar dois numeros: 5+3


num1 = int(input('insira um numero: '))
num2 = int(input('insira outro numero: '))

def somar(x,y):
    print(x+y)

#Chamado da função
somar(num1, num2)

#---------------------------

def subtrair(x,y):
    print(x-y)

#Chamado da função
subtrair(num1,num2)

#---------------------------

def multiplicar(x,y):
    print(x*y)

#Chamado da função
multiplicar(num1,num2)

#---------------------------
def dividir(x,y):
    print(x/y)

#Chamado da função
dividir(num1,num2)

#---------------------------
def divinteira(x,y):
    print(x//y)

#Chamado da função
divinteira(num1,num2)

#---------------------------
def resto(x,y):
    print(x%y)

#Chamado da função
resto(num1,num2)

#---------------------------
def exponeciacao(x,y):
    print(x**y)

exponeciacao(num1,num2)