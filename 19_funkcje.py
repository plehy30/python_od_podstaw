def hello(name, age, last_name=None):
    print('Cześć ' + name + ' ! Masz ' + str(age) + ' lat.')
    # print('Masz na nazwisko: ' + last_name)
    if last_name is not None:
        print('Masz na nazwisko: ' + last_name)

# hello(input('Podaj imię: '), 35)
# hello(input('Podaj imię: '), 40)
# hello(name=input('Podaj imię:'), age=35, last_name='Leczkowski')
# hello(name=input('Podaj imię: '), age=40, last_name='Brzeziński')
hello(name=input('Podaj imię:'), age=35, last_name='Leczkowski')
hello(name=input('Podaj imię: '), age=40,)
