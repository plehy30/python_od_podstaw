# def hello(name, age, last_name=None):
#     print('Cześć ' + name + ' ! Masz ' + str(age) + ' lat.')
#     # print('Masz na nazwisko: ' + last_name)
#     if last_name is not None:
#         print('Masz na nazwisko: ' + last_name)

# hello(input('Podaj imię: '), 35)
# hello(input('Podaj imię: '), 40)
# hello(name=input('Podaj imię:'), age=35, last_name='Leczkowski')
# hello(name=input('Podaj imię: '), age=40, last_name='Brzeziński')
# hello(name=input('Podaj imię:'), age=35, last_name='Leczkowski')
# hello(name=input('Podaj imię: '), age=40,)

# def strip_and_uppercase(text):
#     return str(text).strip().upper()
#
#
# text = '   jestem tekstem DO zmIany'
# print(text)
# text = strip_and_uppercase(text)
# print(text)

countries_information = {}
countries_information['Polska'] = ('Warszawa', 38)
countries_information['Niemcy'] = ('Berlin', 83)
countries_information['Francja'] = ('Paryż', 57)


# country = 'Niemcy'
# print('Kraj: ' + country)
# print('Stolica: ' + countries_information[country][0])
# print('Liczba mieszkańców: ' + str(countries_information[country][1]) + ' milionów')
# print()
# country = 'Francja'
# print('Kraj: ' + country)
# print('Stolica: ' + countries_information[country][0])
# print('Liczba mieszkańców: ' + str(countries_information[country][1]) + ' milionów')

def print_country_information(country):
    print('Kraj: ' + country)
    print('Stolica: ' + countries_information[country][0])
    print('Liczba mieszkańców: ' + str(countries_information[country][1]) + ' milionów')


print_country_information("Niemcy")
print()
print_country_information('Francja')
print()
print_country_information('Polska')
