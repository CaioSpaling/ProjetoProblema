from time import sleep

print('\n')
print(f'{" CAIOBAs HEALTH ":=^40}')
print('Olá, amigo!'.center(42))
print('Se entrou aqui, imagino que queira'.center(40))
print('melhorar sua alimentação!'.center(40))
print('\n')

while True:
    resp = str(input('Deseja criar uma dieta para\nmelhorar sua qualidade de vida? ')).lower().strip()[0]
    if resp == 'n':
        break

    print('\nHm...\n')
    sleep(1.3)
    print('Okay! Então vamos nessa!')

    nome = str(input('Para começarmos, me diga seu nome: '))
    peso = float(input(f'Prazer, {nome}! Agora me diga o seu peso: '))
    altura = float(input(f'Agora, sua altura (cm): '))

