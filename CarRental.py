# Calculadora de Aluguel de Carros
# Defina um idioma - jogue ao script responsável
# Escreva um programa que pergunte a quantidade de Km rodado e qts dias o carro foi alugado
# Calcule o preço à pagar:
# Aluguel diário: R$ 60 | R$ 0,15 por Km
import os
import time as t
import res.lang.en_us as english
import res.lang.pt_br as portuguese
import emoji


# Time tracking and Selection validator
start_time = t.time()
validator = [0, 1]
status = 0


# Language control:

def portuguese_version():
    portuguese.greetings()


def english_version():
    english.greetings()


# Language Selection:
def start_app():
    print(emoji.emojize(":globe_showing_americas: Please, choose a language:\n :flag_united_states: 0 - for English\n :flag_brazil: 1 - for Portuguese (Brazil)"))
    try:
        lang = int(input('Choose: '))
    except:
        print(emoji.emojize(':prohibited: Invalid, try again.'))
        lang = ''

    while lang == '' or lang not in validator:
        try:
            lang = int(input(emoji.emojize(':warning: PLEASE, TYPE 0 OR 1, ONLY: ')))
        except:
            lang = ''

    if lang == 0:
        english_version()
    else:
        portuguese_version()


# Farewell and Elapsed time calcs
def finish_app():
    os.system('cls')
    print(emoji.emojize('Dedell thanks you, closing program.\nDedell agradece, encerrando programa. :⊛_pink_heart:'))

    end_time = t.time()
    elapsed_time = end_time - start_time

    # Time formatting:
    if elapsed_time >= 60:
        minutes = elapsed_time / 60
        print(emoji.emojize(':hourglass_done: elapsed time in minutes: {:.2f}'.format(minutes)))
    else:
        print(emoji.emojize(':hourglass_done: elapsed time in seconds: {:.2f}'.format(elapsed_time)))

    t.sleep(2)
    quit()


# Run everything:
start_app()
