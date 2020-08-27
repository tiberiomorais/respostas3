# 5. Altere o programa anterior permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir a
# operação.
pop_a = int(input('\n Informe a população do país A: '))
pop_b = int(input('\n Informe a população do país B: '))


i_a = float(input('\n Informe a taxa de crescimento do País A: '))
i_b = float(input('\n Informe a taxa de crescimento do País B: '))
i_b = 0.015
qt_ano = 1

while pop_a < pop_b:
    pop_a += pop_a * 0.03
    pop_b += pop_b * 0.015
    print('\n')
    print(f'\n Em {qt_ano} anos a população do país A é de aproximadamente {int(pop_a)} habitantes.')
    print(f'\n Em {qt_ano} anos a população do país B é de aproximadamente {int(pop_b)} habitantes.')
    qt_ano += 1