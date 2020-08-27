# 8. Faça um programa que leia 5 números e informe a soma e a média dos
# números.

lista = []

for i in range (1,6):
    numero = int(input(f'Informe o {i}º número: '))
    lista.append(numero)


#sem funcao
# media = sum(lista) / len(lista)
# print(media)



#com funcao
def calcula_media():
    x = sum(lista) / len(lista)
    return x

print(calcula_media())