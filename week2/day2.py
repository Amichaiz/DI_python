# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter
#
#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor
#
# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)
#
# nc = NewCircle(1)
# print(nc.diameter)
#
# nc.grow()
#
# print(nc.diameter)
#
#
# class A():
#
#     def dothis(self):
#         print("doing this in A")
#
#
# class B(A):
#     pass
#
#
# class C():
#     def dothis(self):
#         print("doing this in C")
#
#
# class D(B, C):
#     pass
#
# d_instance = D()
# d_instance.dothis()
#
# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price
#
#     def present(self):
#         print(f'Title: {self.title}')
#
# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Woow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')
#
# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)

# my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
# temp = 0
# for i in my_list:
#     try:
#         temp += i
#     except:
#         print("Your age is not a real age")
# print(temp)
#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Tiger(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# ti1 = Tiger("tamar",53)
# ti2 = Chartreux("taewamar",23)
# ti3 = Bengal("tswefamar",553)
# ti4 = Bengal("tamsefar",3)
# my_cats = [ti1, ti2, ti3, ti4]
# my_pets = Pets(my_cats)
# my_pets.walk()


# Create a class called BankAccount that contains the following attributes and methods:
# balance - (an attribute)
# __init__ : initialize the attribute
# deposit : - (a method) accepts a positive int and adds to the balance, raise an Exception if the int is not positive.
# withdraw : - (a method) accepts a positive int and deducts from the balance, raise an Exception if not positive

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,dep):
        if dep > 0:
            self.balance += dep
        else:
            raise Exception("Sorry, no numbers below zero")

    def withdraw(self, wit):
            self.balance -= wit

    def count(self):
        print(f'{self.balance}')


class MinimumBalanceAccount (BankAccount):
    def __init__(self, min):
        self.balance = 0
        self.min = min

    def withdraw(self, wit):
        if self.balance > wit > self.min:
            self.balance -= wit
        else:
            raise Exception("Sorry, no numbers below zero")


amichai = MinimumBalanceAccount(300)
amichai.deposit(500)
amichai.count()
amichai.withdraw(100)
amichai.count()
amichai.withdraw(5000)

