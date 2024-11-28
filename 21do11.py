"""
1- Faça um programa que leia um númeoro inteiro e imprima-o.

Num1: int = int(input('Digite o numero: '))
print (Num1)

_____________________________________________________________________________________________


2- Faça um programa que peça para o usuario digitar 3 valores inteiro e imprima a soma deles

Num1: int = int(input('Digite o Primeiro numero: '))
Num2: int = int(input('Digite o Segundo numero: '))
Num3: int = int(input('Digite o Terceiro numero: '))
soma= Num1+Num2+Num3
print (f'A Soma dos Valores é: {soma}')

_____________________________________________________________________________________________


3- faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

Num1: int = int(input('Digite o Primeiro numero: '))
Num2: int = int(input('Digite o Segundo numero: '))
Num3: int = int(input('Digite o Terceiro numero: '))

soma= (Num1*Num1)+(Num2*Num2)+(Num3*Num3)
print (f'A soma dos quadrados dos valores é: {soma}')

_____________________________________________________________________________________________


TAREFAS

1-

num1: int = int(input('Digite o Primeiro numero: '))
num2: int = int(input('Digite o Segundo numero: '))

if num1 > num2 :
    print (f'{num1} é maior que {num2}')
elif num1 < num2 :
    print (f'{num2} é maior que {num1}')
else :
    print (f'{num1} é igual a {num2}')

_____________________________________________________________________________________________


2-

import math

num1: int = int(input('Digite o numero: '))

if num1 > 0 :
    print (f'O numero é positivo, e a Raiz Quadrada dele é: {math.sqrt(num1)}')
    
elif num1 < 0 :
    print ('O numero é negativo')
else :
    print ('O numero é zero')

_____________________________________________________________________________________________


3-

num1: int = int(input('Digite o numero: '))

if (num1 % 2) == 0 :
    print (f'O numero é par')
else :
    print ('O numero é impar')



"""