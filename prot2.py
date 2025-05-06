from time import sleep

print('\n')
print(f'{" CAIOBAs HEALTH ":=^40}')
print('Olá, amigo!'.center(42))
print('Se entrou aqui, imagino que queira'.center(40))
print('melhorar sua alimentação!'.center(40))
print('-'*40)

while True:
    resp = str(input('Deseja criar uma dieta para\nmelhorar sua qualidade de vida? ')).lower().strip()[0]
    if resp == 'n':
        print('\nTudo bem, quem sabe um dia, até logo!')
        break

    print('\nHm...\n')
    sleep(1.3)
    print('Okay! Então vamos nessa!')

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
    
    tmb=0

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
            
    get = 0
    
    print('-'*20)
    print('Para calculcar o seu GET (Gasto de Energia Total),\nescolha a opção que descreve seu nível de atividade física:')
    print('-'*40)
    print('[1] Sedentário (pouco ou nenhum exercício) \n[2] Levemente ativo (exercício leve 1–3 dias/semana) \n[3] Moderadamente ativo (exercício moderado 3–5 dias/semana) \n[4] Muito ativo (exercício intenso 6–7 dias/semana) \n[5] Extremamente ativo (trabalho físico + treino diário intenso)')
    print('-'*40)
    fator_ativ = int(input('  >>>>> Digite sua opção: '))

    resposta_GET = [1,2,3,4,5]

    if fator_ativ not in resposta_GET:
        while fator_ativ not in resposta_GET:
            print('\nOpção Inválida! Digite novamente:')
            fator_ativ = int(input('  >>>>> Digite sua opção: '))
    print('\n')
    
    match fator_ativ:
        case 1:
            get = tmb * 1.2
        case 2:
            get = tmb * 1.375
        case 3:
            get = tmb * 1.55
        case 4:
            get = tmb * 1.725
        case 5:
            get = tmb * 1.9
    
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
            print(f'Certo! Pelo visto você quer perder peso.\nPara isso, você terá de ingerir {kcal_dia:.0f}kcal todos os dias!')
        case 2:
            kcal_dia = get + (get/5)
            print(f'Certo! Pelo visto você quer ficar grandinho.\nPara isso, você terá de ingerir {kcal_dia:.0f}kcal todos os dias!')
        case 3:
            kcal_dia = get
            print(f'Certo! Se manter no peso em que está é importante!\nPara isso, você terá de ingerir {kcal_dia:.0f}kcal todos os dias!')
    
    print('-'*40)        
    print('Agora vamos criar um cardápio para você!\nE alcançar esse objetivo!')
    print('-'*40)
    print('Antes de começarmos, você possui alguma dessas alergias alimentares abaixo?')
    print('[1] Leite e derivados \n[2] Ovos \n[3] Amendoim ou outras oleaginosas \n[4] Frutos do mar ou peixes \n[5] Soja \n[6] Trigo')
    alergia_s_n = str(input('  >>>>> ')).strip().lower()[0]

    if alergia_s_n == 's': #Isso aqui ta dando errado, RESOLVER!
        lista_alergias = []
        quantidade_alergias = int(input('Quantas alergias dessa lista você possui? '))
        print('Quais?')
        for a in range (quantidade_alergias):
            alergias = int(input('  >>>>> '))
            lista_alergias.append(alergias)

    print(lista_alergias)

    print('Você chegou ao fim do protótipo, nos próximos episódios, um cardápio completo será gerado para você,\ncom a possibilidade de se adequar as suas restrições.')
    print('-'*40)
    resp = str(input('Digite "N" para finalizar o programa: ')).lower().strip()[0]
    if resp == 'n':
        break

            
    