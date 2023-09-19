import os
import time as t
import res.data_processing as dp
import CarRental as main

validator = [0, 1]


def greetings():
    print('* Bem-vindo ao sistema Dedell Rentals *')
    t.sleep(0.5)
    print('Aqui você poderá calcular os valores devidos nas locações dos automóveis.')
    print('')
    input('Pressione ENTER para continuar...')

    os.system('cls')

    print('\x1B[3m"First things first"\x1B[0m')
    type_selection()


def type_selection():
    t.sleep(1)
    print('Você deseja trabalhar com Milhas ou Kilômetros?\n- Para milhas, digite 0\n- Para kilômetros, digite 1')
    try:
        unit = int(input('Escolha: '))
    except:
        print('Inválido, tente novamente: ')
        unit = ''

    while unit == '' or unit not in validator:
        try:
            unit = int(input('DIGITE APENAS 0 ou 1: '))
        except:
            unit = ''
    return data_processing(unit)


def data_processing(unit):
    checker = 0
    while checker == 0:
        # Outside process
        if unit == 0:
            ext_processing = dp.m_calc_ptbr()
            result = ext_processing[0]
            checker = ext_processing[1]
            days = ext_processing[2]
        elif unit == 1:
            ext_processing = dp.km_calc_ptbr()
            result = ext_processing[0]
            checker = ext_processing[1]
            days = ext_processing[2]
        else:
            result = 'Bad request!'
        print('O valor a ser cobrado ao cliente é de R$ {:.2f}'.format(result))
        input('Pressione ENTER para finalizar...')
    return main.finish_app()
