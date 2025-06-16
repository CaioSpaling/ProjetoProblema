from time import sleep
import os
import csv
from itertools import islice

def validar_entradas_string(mensagem, tipo=str):
    while True:
        try:
            print('-'*10)
            escrita = (input(mensagem))
            if not escrita.replace(' ', '').isalpha():
                raise ValueError('Digite apenas letras e espaços.')
            return escrita.title()
        except ValueError as e:
            print(f'\nErro: {e}\nDigite novamente!')
            
def validar_respostas_numericas(mensagem, tipo=int, min_val=None, max_val=None):
    while True:
        try:
            valor = tipo(input(mensagem))
            if min_val is not None and valor < min_val:
                print(f'O valor deve ser maior ou igual a {min_val}!')
                continue
            if max_val is not None and valor > max_val:
                print(f'O valor deve ser menor ou igual a {max_val}!')
                continue
            return valor
        except ValueError:
            print('Valor inválido. Digite novamente!')
            print('-'*10)

def dieta(kcal):
    try:
        kcal_int = int(kcal)
    except ValueError:
        return ['Valor de kcal inválido.']
    
    ranges = {
        1500: (0, 25),
        2000: (26, 56),
        2500: (56, 84),
        3000: (85, 115),
        3500: (113, 143),
        4000: (146, 176),
        4500: (176, 213)
    }
    
    inicio, fim = None, None
    for limite, (i, f) in ranges.items():
        if kcal_int <= limite:
            inicio, fim = i, f
            break
    
    if inicio is None:
        return ['Valor de kcal muito alto. Procure um nutricionista.\n']
    
    try:
        with open('dietas.txt', 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            linhas = list(islice(leitor_csv, inicio, fim))
            return[','.join(linha) for linha in linhas]
    except FileNotFoundError:
        ['O arquivo dietas.txt não foi encontrado!']
        
def tmb(sexo, idade, peso):
    tmb = 0 
    if sexo == 'f':
        if idade > 0 and idade <= 3:
            tmb = (58.317 * peso) - 31.1
        elif idade > 3 and idade <= 10:
            tmb = (20.315 * peso) + 485.9
        elif idade > 10 and idade <= 18:
            tmb = (13.384 * peso) + 692.6
        elif idade > 18 and idade <= 30:
            tmb = (14.814 * peso) + 486.6
        elif idade > 30 and idade <= 60:
            tmb = (8.126 * peso) + 845.6
        elif idade > 60:
            tmb = (9.082 * peso) + 685.5
    
    if sexo == 'm':
        if idade > 0 and idade <= 3:
            tmb = (59.512 * peso) - 30.4
        elif idade > 3 and idade <= 10:
            tmb = (22.706 * peso) + 504.3
        elif idade > 10 and idade <= 18:
            tmb = (17.686 * peso) + 658.2
        elif idade > 18 and idade <= 30:
            tmb = (15.057 * peso) + 692.2
        elif idade > 30 and idade <= 60:
            tmb = (11.472 * peso) + 873.1
        elif idade > 60:
            tmb = (11.711 * peso) + 587.7
    return tmb


def main():
    print('\n')
    print(f'{" CAIOBA's HEALTH ":-^40}')
    print('Olá, amigo!'.center(42))
    print('Se entrou aqui, imagino que queira'.center(40))
    print('melhorar sua alimentação!'.center(40))
    print('-'*40)
    sleep(4.0)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        print('-'*10)
        resp = str(input('Deseja criar uma dieta para\nmelhorar sua qualidade de vida? ')).lower().strip()[0]
        if resp not in ['s', 'n']:
            print('Resposta inválida! Digite S ou N.')
            continue
        if resp == 'n':
            print('Certo. Obrigado!')
            break
        
        print('\nHm...\n')
        sleep(1.3)
        print('Okay! Então vamos nessa!')
        sleep(1.2)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        nome = validar_entradas_string('Digite seu nome: ')
        print('-'*10)
        
        sexo = ''
        
        while sexo not in ['m', 'f']:
            sexo = str(input(f'Digite seu sexo [M/F]: ')).strip().lower()[0]
            if sexo not in ['m', 'f']:
                print('Resposta inválida.')
                print('-'*10)
                
        print('-'*10)
        idade = validar_respostas_numericas('Digite sua idade: ', min_val=1, max_val=120)
        print('-'*10)
        peso = validar_respostas_numericas('Digite seu peso (kg): ', float, min_val=20, max_val=300)
        print('-'*10)
        altura = validar_respostas_numericas('Digite sua altura (cm): ', min_val=50, max_val=240)
        print('-'*10)
        sleep(1.3)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('-'*10)
        print('Para calculcar o seu GET (Gasto de Energia Total),\nescolha a opção que descreve seu nível de atividade física:')
        print('-'*30)
        print('[1] Sedentário\n[2] Levemente ativo\n[3] Moderadamente ativo\n[4] Muito ativo\n[5] Extremamente ativo')
        print('-'*30)
        fator_ativ = validar_respostas_numericas('  >>>>> Digite sua opção (1-5): ', min_val=1, max_val=5)
        sleep(1.3)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        get = tmb(sexo, idade, peso) * [1.2, 1.375, 1.55, 1.725, 1.9][fator_ativ-1]
        print(f'O seu GET corresponde a {get:.0f}kcal/dia!')
        
        print('-'*20)
        print(f'Agora é preciso definir qual o seu objetivo:')
        print('-'*20)
        print('[1] Perder peso \n[2] Ganhar peso \n[3] Manter peso')
        obj = validar_respostas_numericas('  >>>>> Digite sua opção (1-3): ', min_val=1, max_val=3)

        print('-'*10)
        match obj:
            case 1:
                kcal_dia = get * 0.8
                print(f'Para perder peso, será necessário a ingerir {kcal_dia:.0f}kcal por dia!')
            case 2:
                kcal_dia = get * 1.2
                print(f'Para ganhar peso, será necessário a ingerir {kcal_dia:.0f}kcal por dia!')
            case 3:
                kcal_dia = get
                print(f'Para manter seu peso, será necessário ingerir {kcal_dia:.0f}kcal por dia')
        print('-'*10)
        print('\nGERANDO SUA DIETA...\n')
        sleep(2.5)
                
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\nAqui está sua dieta personalizada!\n')
        dieta_c = dieta(kcal_dia)
        for linha in dieta_c:
            print(linha)
        
        break

if __name__ == "__main__":
    main()

    
