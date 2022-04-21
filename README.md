# EPTA-Forge-Python

Aqui vai ficar o resumão do curso!

Links:

- [Aula 1](https://www.youtube.com/watch?v=vF6ZNMKDQeU)
- [Aula 2](https://www.youtube.com/watch?v=duneiZ1g4AI)
- [Aula 3]()
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

## Exercício de Cálculo do IMC:
Enunciado: Nosso programa deve fazer o cálculo do IMC de um usuário
```
IMC
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

