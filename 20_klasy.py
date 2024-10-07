class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.mail)
        print(self.age)

    # metoda sprawdzająca czy mężczyzna czy nie
    def is_male(self):
        return self.name[-1:] != 'a'


user = User('Kamila', 'kamila@progrmujodpoddstaw.pl', 35)
# user.name = 'Kamil'
# user.mail = 'kamil@progrmujodpoddstaw.pl'
# user.age = 35

user1 = User('Tomek', 'tomek@progrmujodpoddstaw.pl', 54)
# user1.name = 'Tomek'
# user1.mail = 'tomek@progrmujodpoddstaw.pl'
# user1.age = 54

user.print_info()
user1.print_info()
print(user.name)
print(user1.name)
print(user.is_male())
print(user1.is_male())
