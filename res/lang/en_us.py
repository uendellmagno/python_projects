import os
import time as t
import res.data_processing as dp
import CarRental as main

validator = [0, 1]


def greetings():
    print("* Welcome to Dedell Rentals system *")
    t.sleep(0.5)
    print("Here you can calculate due values in the car rentals")
    print("")
    input("Press ENTER to continue...")

    os.system("cls")

    print('\x1B[3m"First things first"\x1B[0m')
    type_selection()


def type_selection():
    t.sleep(1)
    print("You want to work with Miles or Kilometers?\n- For miles, type 0\n- For kilometers, type 1")
    try:
        unit = int(input("Choose: "))
    except:
        print("Invalid, try again: ")
        unit = ''

    while unit == '' or unit not in validator:
        try:
            unit = int(input("TYPE 0 OR 1 ONLY: "))
        except:
            unit = ''
    return data_processing(unit)


def data_processing(unit):
    checker = 0
    while checker == 0:
        # Outside process
        if unit == 0:
            ext_processing = dp.m_calc()
            result = ext_processing[0]
            checker = ext_processing[1]
        elif unit == 1:
            ext_processing = dp.km_calc()
            result = ext_processing[0]
            checker = ext_processing[1]
        else:
            result = "Bad request!"
        print("The amount to be charged to the customer is US$ {:.2f}".format(result))
        input('Press ENTER to finish...')
    return main.finish_app()
