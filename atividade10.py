# 10. Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

lista = []

for i in range(num1,num2+1):
    lista.append(i)

print(lista)
