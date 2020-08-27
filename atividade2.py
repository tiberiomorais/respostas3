# Faça um programa que leia um nome de usuário e a sua senha e não
# aceite a senha igual ao nome do usuário, mostrando uma mensagem de
# erro e voltando a pedir as informações.

continua = True

while continua:
    nome = input('\n Usuário: ')
    senha = input('\n Senha: ')
    if senha == nome:
        print('\n Usuário e Senha Inválidos!')
    else:
        print('Usuário Correto')
        continua = False

