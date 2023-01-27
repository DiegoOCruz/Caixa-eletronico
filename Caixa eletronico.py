print('=' *45)
print('{:^45}'.format('BANCO ABC BRASIL S/A.'))
print('=' *45)
print('''Notas disponíveis para saque: 
R$ 100,00 / R$ 50,00 / R$ 20,00 / R$ 10,00''')
print('-' *45)
saque = int(input('Que valor deseja sacar: '))
n100 = n50 = n20 = n10 = 0
while True:
    if saque % 10 != 0 or saque <= 0:
        print('[ERRO] Valores Inválidos!')
        saque = int(input('Que valor deseja sacar: '))
    if saque % 10 == 0 or saque > 0:
        while saque >= 100:
            n100 += 1
            saque -= 100
        while saque >= 50:
            n50 += 1
            saque -= 50
        while saque >= 20:
            n20 += 1
            saque -= 20
        while saque >= 10:
            n10 += 1
            saque -= 10
        break
if n100 > 0:
    print(f'Total de {n100} notas de R$100,00')
if n50 > 0:
    print(f'Total de {n50} notas de R$50,00')
if n20 > 0:
    print(f'Total de {n20} notas de R$20,00')
if n10 > 0:
    print(f'Total de {n10} notas de R$10,00')

print('=' * 45)
print('Volte sempre ao BANCO ABC BRASIL S/A.')






