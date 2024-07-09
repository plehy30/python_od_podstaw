phone_book = {
    'Kamil': 100200300,
    'Mariusz': 666777888,
    'Dominik': 400400400
}

print(phone_book.get('Kamil'))
phone_book['Paulina'] = 200200100
phone_book['Kamil'] = 777777777
deleted_phone_number = phone_book.pop('Mariusz')
deleted_phone_number1 = phone_book.pop('Mariusz123', 'Nie ma takiego numeru')
print(deleted_phone_number1)
print(deleted_phone_number)
print(phone_book)
for element in phone_book:
    print(element)
for element in phone_book.values():
    print(element)
for element in phone_book.items():
    print(element)
for element in phone_book.items():
    print(element[0] + ":" + str(element[1]))
for name, phone_number in phone_book.items():
    print(name + ":" + str(phone_number))
