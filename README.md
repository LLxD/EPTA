# EPTA-Forge-Python

Aqui vai ficar o resumão do curso!

Links:

- [Aula 1](https://www.youtube.com/watch?v=vF6ZNMKDQeU)
- [Aula 2](https://www.youtube.com/watch?v=duneiZ1g4AI)
- [Aula 3](https://www.youtube.com/watch?v=QSy4wNesAmk)
- [Replit - Compilador Online](https://replit.com/new/python3)
- [Download Python](https://www.python.org/downloads/)

## Declaração de Variáveis e Tipos:

Para declarar uma variável, basta colocar o nome dela, seguido por um =, seguido pelo valor que você quer atribuir a ela!

``` python

minha_variavel = 150

``` 

Existem vários tipos de variáveis, alguns deles são:

- int (Números Inteiros)
- str (String - Texto)
- char (Caractére)
- float (Números decimais)
- boolean (Verdadeiro ou Falso)



## Operações Matemáticas Básicas:

Podemos fazer várias operações matemáticas com o Python, as mais básicas e que provavelmente mais vão ser usadas são:

- Adição -> Símbolo: +
- Subtração -> Símbolo: -
- Multiplicação -> Símbolo: *
- Exponenciação -> Símbolo: **
- Divisão -> Símbolo: /
- Divisão Inteira -> Símbolo: //
- Módulo (Resto da Divisão) -> %


## Booleanos e operadores comparativos

Booleanos são valores que podem ser apenas True ou False (verdadeiro ou falso). Nós também temos no Python, vários operadores comparativos e eles sempre vão retornar booleanos.

- Maior que -> Símbolo: >
- Menor que -> Símbolo : <
- Maior igual à -> Símbolo: >=
- Menor igual à -> Símbolo: <=
- Diferente de -> Símbolo: !=

## Lógica Condicional

A lógica condicional, permite a nós, programadores, executar trechos de código somente se uma condição inicial for verdadeira. Sua estrutura é da seguinte forma:

  
  ```python

if(CONDICAO):
    #coisas que precisam ser feitas caso seja verdade!
elif(OUTRA CONDICAO):
    #caso não entre na primeira condição, e uma segunda condição for verdadeira!
else:
    #caso não entre em nenhuma das condições

``` 

## Exercício 1 - Cálculo do IMC:
Enunciado: Nosso programa deve fazer o cálculo do IMC de um usuário
```
IMC
FÓRMULA = PESO/(ALTURA²)

POSSÍVEIS RESULTADOS
< 18,5 = MAGREZA
>= 18,5 E <= 24,9 NORMAL
>= 25 E <= 29,9 SOBREPESO
>29,9 OBESIDADE
```
<details>
  <summary>Aviso de Spoiler da Resposta</summary>
  

  ```python


altura = float(input("Digite sua altura "))
peso = float(input("Digite seu peso "))

imc = peso / (altura ** 2)

if(imc < 18.5):
    print("magreza")
elif (imc >= 18.5 and imc <= 25):
    print("normal")
elif (imc > 25 and imc <= 29.9):
    print("sobrepeso")
else:
    print("obesidade")

``` 
  
</details>

## Listas

A lista (ou array) é uma estrutura de dados show para armazenarmos vários valores em sequência!
Temos vários métodos que podem nos ajudar no dia-a-dia com listas, eles são:
- append() -> Adiciona ao final da lista
- remove() -> Remove um item da lista
- insert() -> Insere em uma posição especificada
- sort() -> Ordena a lista

Exemplos com lista:

```python

lista_de_numeros = [1,2,3,4,5]
lista_de_numeros.remove(4)


lista_de_compras = ["banana","maca","leite","biscoito"]
lista_de_compras.append("cebola")
lista_de_compras.sort()
print(lista_de_compras)



```

## Laços de Repetição:

Para podermos executar o mesmo código várias vezes, utilizamos os laços de repetição.
Esses são: for e while.

Exemplos com for e while:

### For:
```python

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

```

##### Atenção com as palavras reservadas break e continue

### While:
```python
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

```

##### Cuidado com os loops infinitos hein!

## Funções:

Para podermos encapsular nosso código e nos organizarmos melhor, podemos separar blocos de código em funções

Exemplos de funções:
```python

def ola():
    print("Ola!")


def ola_com_parametros(nome):
    print("Ola!" + " " + nome)

ola()

ola_com_parametros("Lucas")

```


## Exercício 2 - Encapsular o código de cálculo de IMC em uma função

A ideia desse exercício é simplesmente encapsular toda a lógica do exercício de IMC em uma função, para que possamos deixar nosso código mais organizado!

<details>
  <summary>Aviso de Spoiler da Resposta</summary>
  

  ```python


altura = float(input("Digite sua altura "))
peso = float(input("Digite seu peso "))

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


valor_final = calcula_imc(peso,altura)
print(valor_final)

``` 
</details>

## Funções Recursivas
Funções recursivas são funções que chamam elas mesmas em seu interior. (É um conceito complexo e leva tempo pra digerir e entender direitinho! Vocês podem ler mais [aqui](https://realpython.com/python-thinking-recursively/)).
O importante, é lembrarmos da condição de parada (também chamada de caso base), que é um caso da nossa função que vai ser o momento de retorno, onde a função acaba para não acabarmos com um loop infinito.

Exemplo de função recursiva:

  ```python

def fatorial(numero):
    print(numero)
    if numero == 1: #<- CASO BASE
        return 1 
    else:
        return(numero*fatorial(numero-1))

fatorial(10)

``` 

## Bibliotecas Interessantes e módulos legais :D

Nessa seção, vou apresentar alguns módulos e coisas legais que o python fornece pra gente trabalhar. São só alguns exemplos de coisas que o Python pode fazer, mas num geral, existem muitas coisas além disso. Vocês podem conferir algumas coisas [aqui](https://github.com/vinta/awesome-python).

<details>
  <summary>Aleatoriedade</summary>
Para aleatoriedade, normalmente utilizamos o módulo random.

  ```python

import random
#random https://docs.python.org/3/library/random.html

dado_6_lados = random.randint(1,6)
print(dado_6_lados)


``` 
  
</details>

<details>
  <summary>Testes Unitários</summary>
É importante mantermos testes do nosso código automatizados, garantindo que o nosso código de fato produza o resultado desejado sem termos que verificar manualmente, para isso, podemos usar o módulo unittest.

  ```python

import random
import unittest
#unittest https://docs.python.org/3/library/unittest.html

dado_6_lados = random.randint(1,6)
print(dado_6_lados)


def teste_unitario_dado(dado):
    assert dado <= 6,"O valor do dado obtido foi maior que 6"
    print("O dado tem o valor <= 6 :D")
    print("Todos os testes passaram!")

teste_unitario_dado(dado_6_lados)


``` 

Normalmente, os testes ficam em outro arquivo (que pode ser executado separadamente, via terminal). Além disso, existe um método de desenvolvimento de software guiado por testes chamado TDD, que vocês podem saber mais sobre [aqui] (https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/).

  
</details>

<details>
  <summary>Matemática científica</summary>
O Python é show com matemática e dá pra utilizar o módulo math, a lib numpy e a lib matplotlib pra gerarmos muito conteúdo científico em termos de matemática! Seguem alguns exemplos:

  ```python

import math
#math https://docs.python.org/3/library/math.html
#matplotlib https://matplotlib.org/
#numpy https://numpy.org/

#math -> Alguns cálculos mais complicados


print(math.sqrt(15))
print(math.sin(math.pi/6))
print(math.cos(math.radians(60)))


#numpy matemática mais avançada e funções auxiliares show
#matplotlib plotagem de gráficos

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + np.sin(x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()
plt.savefig("matplotlib.png")

``` 
  
</details>


## Programação Orientada a Objetos (POO)

Nesse paradigma, utilizamos a ideia de classe para criarmos novos tipos de estruturas de dados que podem nos auxiliar na construção de uma aplicação.
O método ```__init__``` é chamado de contrutor.
POO é muito extensa e essa seção é só uma ideia pra aflorar na cabeça de vocês! POO é muito utilizada em jogos e aplicações mais robustas justamente pela sua maior facilidade em deixar código grande organizado e com uma certa facilidade em termos de manutenção.
Quando criamos uma nova variável com base em uma classe que criamos, chamamos esse processo de __instanciar__ um objeto da classe.

Exemplos:

```python

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
    
    def ola(self):
        print("Ola, eu sou "+self.nome+ " e tenho " + str(self.idade) + " anos")

lucas = Pessoa(nome="Lucas",idade=23) #<- lucas é uma instancia de pessoa
print(lucas.idade)
lucas.ola()



class Retangulo:
    def __init__(self, altura:float, largura:float):
        self.altura = altura
        self.largura = largura

    def area(self):
        return(self.altura * self.largura)

    def perimetro(self):
        return(self.altura * 2 + self.largura * 2)

meu_primeiro_retangulo = Retangulo(altura = 10,largura = 20) #<- meu_primeiro_retangulo é uma instancia de Retangulo
meu_segundo_retangulo = Retangulo(altura = 5,largura = 12) #<- meu_segundo_retangulo é uma outra instancia de Retangulo
print(meu_primeiro_retangulo.area())
print(meu_segundo_retangulo.area()) 

```
