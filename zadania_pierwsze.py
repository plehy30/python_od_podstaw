# score = int(input("Podaj wynik (0-100)"))
#
# if score > 100 or score < 0:
#     print("Wynik powinien być w zakresie 0-100")
# elif score >= 90:
#     print("Twoja ocena to piątka")
# elif score >= 80:
#     print("Twoja ocena to cztery")
# elif score >= 70:
#     print("Twoja ocena to trzy")
# elif score >= 60:
#     print("Twoja ocena to dwa")
# else:
#     print("Twoja ocena to jedynka")

# liczby pierwsze od 1 do 100
# sprawdzamy czy liczba jest podzielna przez jakąkolwiek liczbę z przedziału 2 - i-1
# for i in range(2, 101):
#     is_prime = True
#
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(i)
# suma liczb parzystych
# sum = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
#
# print(sum)

# Program który sprawdzi czy podane imię jest imieniem żeńskim czy męskim, zakładając że żeńskie kończą sie na literę a
# name = input("Podaj imię: ")
#
# if name.endswith("a"):
#     print("To jest imię żeńskie")
# else:
#     print("To jest imię męskie")
# Pobierz od użytkownika trzy liczby całkowite i oporządkuj je w kolejności od najmniejszej do największej
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))
# c = int(input("Podaj trzecią liczbę: "))

# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
#
# print(f"Liczby w kolejności od najmniejszej do największej: {a}, {b}, {c}")
import random

random_number = random.randint(1, 100)
user_number = None

while user_number != random_number:
    user_number = int(input("Podaj liczbę: "))

    if user_number < random_number:
        print("Za mało")
    elif user_number > random_number:
        print("Za dużo")
    else:
        print("Udało Ci się odgadnąć liczbę")
