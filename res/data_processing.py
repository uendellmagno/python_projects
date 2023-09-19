import time as t
import os


# ENGLISH PARAMETERS

def m_calc():
    # Clear console and End Loop
    os.system('cls')
    checker = 1

    # Data Entry - Base calculation parameters
    try:
        daily_rate = float(input("Enter the daily rate: $"))
        m_rate = float(input('Enter the value of the mile driven: $ '))
    except:
        print('Oops, something went wrong! Try again.')
        daily_rate = ''
        m_rate = ''
    while daily_rate == '' or m_rate == '':
        try:
            daily_rate = float(input("Please, enter the daily rate: $ "))
            m_rate = float(input('Please, enter the value of the mile driven: $ '))
        except:
            print("Oops, something went wrong! Let's try again.")
            daily_rate = ''
            m_rate = ''
    t.sleep(0.5)
    os.system('cls')

    # Data Entry - Rental Parameters
    print('Okay, now, tell me abot the rent:')
    t.sleep(0.5)
    try:
        driven = float(input('Enter the number of miles driven: '))
        rented = int(input('Enter the number of days rented: '))
    except:
        print('Oops, something went wrong! Try again.')
        driven = ''
        rented = ''
    while driven == '' or rented == '':
        try:
            driven = float(input('Please, enter the number of miles driven: '))
            rented = int(input('Please, enter the number of days rented: '))
        except:
            print("Oops, something went wrong! Let's try again.")
            driven = ''
            rented = ''

    # Calculation System
    d_rental = daily_rate * rented
    d_driven = m_rate * driven
    op_rental = float(d_rental + d_driven)

    # Finish and return to main
    os.system('cls')
    print('Awesome. Calculating...')
    t.sleep(1.5)
    os.system('cls')

    return op_rental, checker


def km_calc():
    # Clear console and End Loop
    os.system('cls')
    checker = 1

    # Data Entry - Base calculation parameters
    try:
        daily_rate = float(input("Enter the daily rate: R$"))
        km_rate = float(input('Enter the value of the kilometer driven: R$ '))
    except:
        print('Oops, something went wrong! Try again.')
        daily_rate = ''
        km_rate = ''
    while daily_rate == '' or km_rate == '':
        try:
            daily_rate = float(input("Please, enter the daily rate: R$"))
            km_rate = float(input('Please, enter the value of the kilometer driven: R$ '))
        except:
            print("Oops, something went wrong! Let's try again.")
            daily_rate = ''
            km_rate = ''
    t.sleep(0.5)
    os.system('cls')

    # Data Entry - Rental Parameters
    print('Okay, now, tell me abot the rent:')
    t.sleep(0.5)
    try:
        driven = float(input('Enter the number of kilometers driven: '))
        rented = int(input('Enter the number of days rented: '))
    except:
        print('Oops, something went wrong! Try again.')
        driven = ''
        rented = ''
    while driven == '' or rented == '':
        try:
            driven = float(input('Please, enter the number of kilometers driven: '))
            rented = int(input('Please, enter the number of days rented: '))
        except:
            print("Oops, something went wrong! Let's try again.")
            driven = ''
            rented = ''
    # Calculation System
    d_rental = daily_rate * rented
    d_driven = km_rate * driven
    op_rental = d_rental + d_driven
    # main.ext_process(op_rental, 1)

    # Finish and return to main
    os.system('cls')
    print('Awesome. Calculating...')
    t.sleep(1.5)
    os.system('cls')

    return op_rental, checker


# PORTUGUESE BR PARAMETERS


def m_calc_ptbr():
    # Clear console and End Loop
    os.system('cls')
    checker = 1

    # Data Entry - Base calculation parameters
    try:
        daily_rate = float(input("Digite o valor da diária: $"))
        m_rate = float(input('Digite o valor da milha rodada: $ '))
    except:
        print('Ops, algo deu errado! Tente novamente.')
        daily_rate = ''
        m_rate = ''
    while daily_rate == '' or m_rate == '':
        try:
            daily_rate = float(input("Por favor, digite o valor da diária: $ "))
            m_rate = float(input('Agora, digite o valor da milha rodada: $ '))
        except:
            print('Ops, algo deu errado! Vamos tentar novamente.')
            daily_rate = ''
            m_rate = ''
    t.sleep(0.5)
    os.system('cls')

    # Data Entry - Rental Parameters
    print('Ok, agora, me conte sobre o aluguel:')
    t.sleep(0.5)
    try:
        driven = float(input('Digite a quantidade de milhas rodadas: '))
        rented = int(input('Digite o número de dias locados: '))
    except:
        print('Ops, algo deu errado! Tente novamente.')
        driven = ''
        rented = ''
    while driven == '' or rented == '':
        try:
            driven = float(input('Por favor, digite a quantidade de milhas rodadas: '))
            rented = int(input('Por favor, digite o número de dias locados: '))
        except:
            print('Ops, algo deu errado! Vamos tentar novamente.')
            driven = ''
            rented = ''

    # Calculation System
    d_rental = daily_rate * rented
    d_driven = m_rate * driven
    op_rental = float(d_rental + d_driven)

    # Finish and return to main
    os.system('cls')
    print('Perfeito. Calculando...')
    t.sleep(1.5)
    os.system('cls')

    return op_rental, checker


def km_calc_ptbr():
    # Clear console and End Loop
    os.system('cls')
    checker = 1

    # Data Entry - Base calculation parameters
    try:
        daily_rate = float(input("Digite o valor da diária: R$"))
        km_rate = float(input('Digite o valor do kilômetro rodado: R$ '))
    except:
        print('Ops, algo deu errado! Tente novamente.')
        daily_rate = ''
        km_rate = ''
    while daily_rate == '' or km_rate == '':
        try:
            daily_rate = float(input("Por favor, digite o valor da diária: R$"))
            km_rate = float(input('Por favor, digite o valor do kilômetro rodado: R$ '))
        except:
            print('Ops, algo deu errado! Vamos tentar novamente.')
            daily_rate = ''
            km_rate = ''
    t.sleep(0.5)
    os.system('cls')

    # Data Entry - Rental Parameters
    print('Ok, agora, me conte sobre o aluguel:')
    t.sleep(0.5)
    try:
        driven = float(input('Digite quantos kilômetros foram rodados: '))
        rented = int(input('Digite o número de dias locados: '))
    except:
        print('Ops, algo deu errado! Vamos tentar novamente.')
        driven = ''
        rented = ''
    while driven == '' or rented == '':
        try:
            driven = float(input('Por favor, digite quantos kilômetros foram rodados: '))
            rented = int(input('Por favor, digite o número de dias locados: '))
        except:
            print('Ops, algo deu errado! Vamos tentar novamente.')
            driven = ''
            rented = ''
    # Calculation System
    d_rental = daily_rate * rented
    d_driven = km_rate * driven
    op_rental = d_rental + d_driven
    # main.ext_process(op_rental, 1)

    # Finish and return to main
    os.system('cls')
    print('Perfeito. Calculando...')
    t.sleep(1.5)
    os.system('cls')

    return op_rental, checker
