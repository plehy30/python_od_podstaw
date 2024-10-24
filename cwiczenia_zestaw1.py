# 1.Napisz program, który sprawdza, czy podana przez użytkownika liczba jest parzysta czy nieparzysta.
# number_1 = int(input("Podaj liczbę: ")
# if number_1 % 2==0:
#     print('To jest liczba parzysta')
# else:
#     print('To jest liczba nieparzysta.')
# 2. Napisz program, który sprawdza, czy podana przez użytkownika liczba jest większa od 0, mniejsz od 0,
# równa 0.
# if number_1 == 0:
#     print('Ta liczba jest równa zero')
# elif number_1 > 0:
#     print("ta liczba jest większa od zera")
# else:
#     print("Ta liczba kest mniejsza od zera.")
#
# 3. Napisz program, który zapyta użytkownika o wynik na egzaminie (od 0 do 100) i wyświetli
# odpowiednią ocenę: 90-100 -> 5 80-89 -> 4 70-79 ->3 60-69 ->2 poniżej 60 -> 1
# egzam = int(input('Podaj wynik egzaminu: '))
# if egzam >= 90:
#     print('Dostałeś 5.')
# elif egzam >= 80:
#     print('Dostałeś 4.')
# elif egzam >= 70:
#     print('Dostałeś 3.')
# elif egzam >= 60:
#     print('Dostałeś 2.')
# else:
#     print('Dostałeś 1.')
# 4. Napisz program który wyświetli liczby od 0 do 100
# for i in range(0, 101):
#     print(i)

# 5. Napisz program który wyświetli wszystkie liczby pierwsze od 1 do 100
# sprawdzamy czy liczba i jest podzielna przez jakąkolwiek liczbę z przedziału: (2, i-1)
# for i in range(2, 101):  # 1 nie jest liczbą pierwszą
#     is_prime = True
#
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)

# 6. Napisz program, który wyświetli sumę wszystkich liczb parzystych z przedziału 1 - 100
# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# 7. Napisz program który policzy pole prostokąta (użytkownik musi podać długości boków)

# 8. Napisz program, który sprawdzio, czy podane imię jest imieniem żeńskim czy męskim (załóż, że imiona
# żeńskie kończą się na literę a)
# name = input('Podaj imię: ')
# if name.endswith('a'):
#     print('Jest to imię żeńskie')
# else:
#     print('To jest imię męskie')

# 9. Pobierz od użytkownika trzy liczby całkowite i uporządkuj je w kolejności od najmniejszej do największej.
a = 5  # teraz możemy napisać: int(input('Podaj liczbę a:))
b = 15  # teraz możemy napisać: int(input('Podaj liczbę b:))
c = 10  # teraz możemy napisać: int(input('Podaj liczbę c:))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"Kolejnośc liczb od najmniejszej do największej to: {a}, {b}, {c}")

# 10. Stwórz grę, w ktyórej wylosujesz liczbę z przedziału 1 -100, zapiszesz tę liczbę do zmiennej,
# a następnie poprosisz użytkownika o odgadnięcie tej liczby. Po każdej próbie wyświetlaj informację,
# czy liczba podana przez użytkownika jest mniejsz czy większa od wylosowanej. Gdy użytkownik odgadnie
# liczbę, zakończ grę.
import random

random_number = random.randint(1, 100)
