#laços de repetição
#pontos de parada e continuidade
#range()

lista_de_compras = ["banana","maca","leite","biscoito"]

for compra in lista_de_compras:
    print(compra)

for contador in range(10):
    print(contador)

for compra in lista_de_compras:
    if (compra == "leite"):
        print("encontrei o leite!")
        continue
    print(compra)

for compra in lista_de_compras:
    if (compra == "leite"):
        print("encontrei o leite!")
        break
    print(compra)

contador = 0
while(contador < 4):
    contador = contador + 1
    print(contador)

contador = 0
while(True):
    contador = contador + 1
    print(contador)
    if (contador > 10):
        break

def ola(nome):
    print("Ola!" + " " + nome)

ola("Lucas")

#criar uma função que encapsule a lógica
#do cálculo do imc

def calcula_imc(peso,altura):
    imc = peso / (altura ** 2)
    if (imc < 18.5):
        print("magreza")
    elif (imc >= 18.5 and imc <= 25):
        print("normal")
    elif (imc > 25 and imc <= 29.9):
        print("sobrepeso")
    else:
        print("obesidade")
    return imc

altura = float(input("Digite sua altura "))
peso = float(input("Digite seu peso "))
valor_final = calcula_imc(peso,altura)
print(valor_final)

# fatorial(10) -> 10*fatorial(9) ->10*9*fatorial(8)... -> 10*9*7*6...*1
# 10*9*8*7...
def fatorial(numero):
    print(numero)
    if numero == 1:
        return 1
    else:
        return(numero*fatorial(numero-1))

fatorial(10)