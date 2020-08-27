# 7. Faça um programa que leia 5 números e informe o maior número.

lista = []

for i in range (1,6):
    lista.append(int(input(f'Informe o {i}º número: ')))

print(lista)

maior = max(lista)
print(maior)