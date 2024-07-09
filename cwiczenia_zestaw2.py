# 1.Stwórz listę, którą wypełnisz dziesięcioma liczbami całkowitymi i zwróć somę wszystkich liczb z tej listy
numbers = [2, 5, 7, 19, 21, 34, 77, 80, 90, 120]
sum = 0
for number in numbers:
    sum += number
print(sum)
# 2. Stwórz listę, która będzie zawierać 10 słów. Następnie stwórz drugą listę,
# która będzie zawierać tylko te słowa, które mają więcej niż 5 liter.
words = ['komputer', 'progamowanie', 'informatyka', 'mysz', 'kot', 'pies', 'klawiatura', 'python', 'java',
         'javascript']
more_than_5_letter = []

for word in words:
    if len(word) > 5:
        more_than_5_letter.append(word)
print(more_than_5_letter)
# 3. Stwórz listę, którą wypełnisz dziesięcioma liczbami całkowitymi. Znajdź nalmniejszą i największą.
numbers_3 = [56, 43, 10, 7, 99, 65, 43, 17, 37, 101]
smallest = numbers_3[0]
largest = numbers_3[0]
for number in numbers_3:
    if number < smallest:
        smallest = number

    if number > largest:
        largest = number

print(f"Najmniejsza liczba to:{smallest}, a największa to:{largest}")
# 4. Stwórz dwie listy, które wypełnisz imionami - po 5 w każdej z list. Zadbaj o to ,aby niektóre imiona się powtarzały (czyli, żeby
# były obecne w obu listach). Wyświetl imiona.
names = ['Kamil', 'Mariusz', 'Dominik', 'Asia', 'Kasia']
names2 = ['Paulina', 'Ania', 'Mariusz', 'Dominik', 'Rafał']
print(set(names) & set(names2))
# 5. Korzystając z list z poprzedniego ćwiczenia, wyświetl tylko te imiona, które są obecne w pierwszej liście.
print(set(names) - set(names2))
# 6. Strwórz słownik, który będzie przechowywał informację o krajach i ich stolicach. Dodaj do niego 5 elementów.
# Wyświetl dane ze słownika w formacie kraj - stolica czyli na przykład Polsa - Warszawa.
countries_and_capitals = {
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'Francja': 'Paryż',
    'Słowacja': 'Bratysława',
    'Czechy': 'Praga'
}
for country, capital in countries_and_capitals.items():
    print(f'{country} - {capital}')
# 7. Posortuj słownik z poprzedniego ćwiczenia w kolejności alfabetycznej.
countries_and_capitals = dict(sorted(countries_and_capitals.items()))
print()
for country, capital in countries_and_capitals.items():
    print(f'{country} - {capital}')
# 8. Stwórz program, który prosi użytkownika o wpisanie tekstu w konsoli, a następnie utwórz słownik w którym kluczami będą słowa # występujące w tym tekscie, a wartościami liczby wystąpień każdego słowa. Wyświetl zawartość słownika.
text = input("Napisz tekst: ")
words = text.split(' ')
print(words)
words_count = {}
for word in words:
    if words_count.get(word) is not None:
        words_count[word] += 1
    else:
        words_count[word] = 1
for word, count in words_count.items():
    print(f'{word}: {count}')
