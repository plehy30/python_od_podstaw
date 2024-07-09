names = {'Kamil', 'Mariusz', 'Dominik'}
names2 = {'Kamil', 'Paulina', 'Piotrek', 'Rafał'}
# suma zbiorów
print(names | names2)
print(names.union(names2))
# część wspólna
print(names.intersection(names2))
print(names & names2)
# różnica
print(names.difference(names2))
print(names - names2)
# symetryczna różnica
print(names.symmetric_difference(names2))
print(names ^ names2)
# names.add('Rafał')
# names.remove('Mariusz')
# for name in names:
#     print(name)
#
# names.update({'Adam', 'Tomek'})
# print(names)
