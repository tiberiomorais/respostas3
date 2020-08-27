# 4. Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que a população
# de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça
# um programa que calcule e escreva o número de anos necessários para
# que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

pop_a = 8000
pop_b = 20000

i_a = 0.03
i_b = 0.015
qt_ano = 1

while pop_a < pop_b:
    pop_a += pop_a * 0.03
    pop_b += pop_b * 0.015
    print('\n')
    print(f'\n Em {qt_ano} anos a população do país A é de aproximadamente {int(pop_a)} habitantes.')
    print(f'\n Em {qt_ano} anos a população do país B é de aproximadamente {int(pop_b)} habitantes.')
    qt_ano += 1