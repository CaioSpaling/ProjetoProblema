from time import sleep
import os

dieta_1 = ['Café da manhã', '- 3 ovos inteiros + 3 claras mexidas', 
           '- 2 fatias de pão integral ou 4 col. de aveia', 
           '- 1 banana com pasta de amendoim (1 col. sopa)', 
           '- 200 ml de leite desnatado ou vegetal enriquecido', '',
           'Lanche da manhã', '',
           '- Shake com 1 scoop de whey + 1 banana + aveia + 1 col. de pasta de amendoim',
           '- 5 castanhas', '',
           'Almoço', '',
           '- 150g frango grelhado ou peixe (tilápia, atum)',
           '- 100g arroz integral ou 150g batata-doce',
           '- 1 concha de feijão',
           '- Salada à vontade com azeite de oliva',
           '- Suco natural sem açúcar (opcional)',
           'Lanche da tarde', '',
           '- Sanduíche com 2 fatias de pão integral, 2 ovos cozidos e alface/tomate',
           '- 1 fruta (maçã, pera, melão)', '',
           'Jantar', '',
           '- 150g peito de frango grelhado ou tofu grelhado',
           '- 150g de batata-doce ou arroz integral',
           '- Brócolis, cenoura, abobrinha refogada', '',
           'Ceia', '',
           '- 1 copo de iogurte natural + 2 colheres de aveia ou 1 scoop de caseína']

dieta_2 = ['Café da manhã', '- 2 ovos mexidos com espinafre', 
           '- 1 fatia de pão integral', 
           '- 1 xícara de chá verde ou café sem açúcar', '',
           'Lanche da manhã', '',
           '- 1 maçã ou 1 iogurte zero açúcar', '',
           'Almoço', '',
           '- 120g peito de frango ou peixe',
           '- 100g de arroz integral ou 1/2 xícara de lentilha',
           '- Mix de legumes cozidos no vapor',
           '- Folhas verdes com azeite (1 colher de chá)', '',
           'Lanche da tarde', '',
           '- 1 ovo cozido + 1 fruta pequena', '',
           'Jantar', '',
           '- Omelete com 2 ovos, legumes (abobrinha, cenoura ralada, tomate)',
           '- 1 fatia de queijo branco light (opcional)', '',
           'Ceia', '',
           '- Chá de camomila ou 1 scoop de whey com água (se estiver com fome)']

dieta_3 = ['Café da manhã', '- 2 ovos + 1 fatia de pão integral + 1 banana', 
           '- 1 café com leite (sem açúcar)', '',
           'Lanche da manhã', '',
           '- 1 iogurte com aveia',
           '- 3 castanhas', '',
           'Almoço', '',
           '- 130g frango ou peixe',
           '- 1 concha de feijão',
           '- 1/2 xícara de arroz integral',
           '- Salada com azeite', '',
           'Lanche da tarde', '',
           '- 1 sanduíche de pão integral com ovo cozido',
           '- 1 fruta', '',
           'Jantar', '',
           '- 150g de carne branca ou tofu',
           '- Legumes cozidos',
           '- 50g de arroz integral', '',
           'Ceia', '',
           '- 1 copo de leite vegetal ou 1 iogurte light']

def listas(die):
    for i in die:
        print(i)
    return

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

print('\n')
print(f'{" CAIOBAs HEALTH ":=^40}')
print('Olá, amigo!'.center(42))
print('Se entrou aqui, imagino que queira'.center(40))
print('melhorar sua alimentação!'.center(40))
print('-'*40)

while True:
    resp = str(input('Deseja criar uma dieta para\nmelhorar sua qualidade de vida? ')).lower().strip()[0]
    while resp != 's' and resp != 'n':
        print('-'*20)
        print('Resposta inválida!')
        print('-'*20)
        resp = str(input('Deseja criar uma dieta para\nmelhorar sua qualidade de vida? ')).lower().strip()[0]
    if resp == 'n':
        print('\nCerto, Obrigado!')
        break
    
    print('\nHm...\n')
    sleep(1.3)
    print('Okay! Então vamos nessa!')
    sleep(1.5)
    
    os.system('cls')

    print('-'*20)
    nome = str(input('Para começarmos, me diga seu nome: ')).title()
    print('-'*20)
    sexo = str(input(f'Prazer, {nome}! Me diga seu sexo [M/F]: ')).strip().lower()[0]
    print('-'*20)
    idade = int(input('Agora digite sua idade: '))
    print('-'*20)
    peso = float(input('Digite seu peso (kg): '))
    print('-'*20)
    altura = int(input(f'Por fim, sua altura (cm): '))
            
    get = 0
    
    print('-'*20)
    print('Para calculcar o seu GET (Gasto de Energia Total),\nescolha a opção que descreve seu nível de atividade física:')
    print('-'*40)
    print('[1] Sedentário (pouco ou nenhum exercício) \n[2] Levemente ativo (exercício leve 1–3 dias/semana) \n[3] Moderadamente ativo (exercício moderado 3–5 dias/semana) \n[4] Muito ativo (exercício intenso 6–7 dias/semana) \n[5] Extremamente ativo (trabalho físico + treino diário intenso)')
    print('-'*40)
    fator_ativ = int(input('  >>>>> Digite sua opção: '))
    sleep(1.5)
    
    os.system('cls')

    resposta_GET = [1,2,3,4,5]

    if fator_ativ not in resposta_GET:
        while fator_ativ not in resposta_GET:
            print('\nOpção Inválida! Digite novamente:')
            fator_ativ = int(input('  >>>>> Digite sua opção: '))
    print('\n')
    
    match fator_ativ:
        case 1:
            get = tmb(sexo, idade, peso) * 1.2
        case 2:
            get = tmb(sexo, idade, peso) * 1.375
        case 3:
            get = tmb(sexo, idade, peso) * 1.55
        case 4:
            get = tmb(sexo, idade, peso) * 1.725
        case 5:
            get = tmb(sexo, idade, peso) * 1.9
    
    print(f'O seu GET corresponde a {get:.0f}kcal/dia!')
    print(f'Agora é preciso definir qual o seu objetivo:')
    print('-'*40)
    print('[1] Perder peso \n[2] Ganhar peso \n[3] Manter peso')
    obj = int(input('  >>>>> Digite sua opção: '))

    resposta_obj = [1,2,3]

    if obj not in resposta_obj:
        while obj not in resposta_obj:
            print('Resposta Inválida! Digite novamente:')
            obj = int(input('  >>>>> Digite sua opção: '))
    print('\n')

    kcal_dia = 0

    match obj:
        case 1:
            kcal_dia = get - (get/5)
            print(f'Certo! Pelo visto você quer perder peso.\nPara isso, você terá de ingerir {kcal_dia:.0f}kcal todos os dias!\n')
            print('Aqui está sua dieta!\n')
            listas(dieta_2)
        case 2:
            kcal_dia = get + (get/5)
            print(f'Certo! Pelo visto você quer ficar grandinho.\nPara isso, você terá de ingerir {kcal_dia:.0f}kcal todos os dias!\n')
            print('Aqui está sua dieta!\n')
            listas(dieta_1)
        case 3:
            kcal_dia = get
            print(f'Certo! Ta tranquilo quanto ao seu peso, vamos manter assim então!\nPara isso, você terá de ingerir {kcal_dia:.0f}kcal todos os dias!\n')
            print('Aqui está sua dieta!\n')
            listas(dieta_3)
    break

