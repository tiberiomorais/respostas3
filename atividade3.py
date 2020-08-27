# 3. Faça um programa que leia e valide as seguintes informações:
# A. Nome: maior que 3 caracteres;
# B. Idade: entre 0 e 150;
# C. Salário: maior que zero;
# D. Sexo: 'f' ou 'm';
# E. Estado Civil: 's', 'c', 'v', 'd';




def valida_nome(nome):
    while len(nome)<3:
        print('\n Nome Inválido!')
        nome = input('\n Informe o nome (maior do que 3 carcteres: ')


def valida_idade(idade):
    while 0 > int(idade) or int(idade) > 150:
        print('\n Idade Inválida!')
        idade = input('\n Informe a idade (entre 0 e 150): ')


def valida_salario(salario):
    while int(salario) <= 0:
        print('\n Salário Inválido! ')
        salario = input('\n Informe o salário ( maior do que zero): ')


def valida_sexo(sexo):
    while sexo != 'F' and sexo != 'M' :
        print('\n Sexo Inválido!')
        sexo = input('\n Informe o sexo ( F ou M): ').upper()


def valida_estado_civil(estado_civil):
    while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
        print('\n Estado Civil Inválido! ')
        estado_civil = input('\n Informe o estado civel (S, C,V, ou D): ').upper()



continua = 1

while continua == 1:

    nome = input('\n Informe o nome (maior do que 3 char): ')
    valida_nome(nome)
    idade = input('\n Informe a idade (entre 0 e 150): ')
    valida_idade(idade)
    salario = input('\n Informe o salário ( maior do que zero): ')
    valida_salario(salario)
    sexo = input('\n Informe o sexo ( F ou M): ').upper()
    valida_sexo(sexo)
    estado_civil = input('\n Informe o estado civel (S, C, V, ou D): ').upper()
    valida_estado_civil(estado_civil)
    continua = input('\n Digite 1 para Continuar e 0 para Sair:')
    continua = int(continua)








