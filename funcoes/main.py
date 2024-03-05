from logica import verifica_numero
from logica import paridade
from logica import escrever_nome
#vou criar meu primeiro menu

print("Bem vindo(a) ao modulo de logica...")
num = int(input("Digite o numero :"))
nome = input("Digite o seu nome: ")

print("1️⃣verifica se o numero é positivo\n2️⃣ Paridade\n3️⃣ Mostrar meu nome")
op = int(input("❕Digite a opção :"))

match(op):
    case 1: verifica_numero(num)
    case 2: paridade(num)
    case 3: escrever_nome(nome)
    case _: print("⛔Opção invalida")

