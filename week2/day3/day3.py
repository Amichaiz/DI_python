# class Circle:
#     color = "red"
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#
#     def grow(self, factor=2):
#         self.diameter = self.diameter * factor
#
#     def get_color(self):
#        return Circle.color
#
# circle1 = Circle(2)
# print(circle1.color)
# print(Circle.color)
# print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)

# class MyClass:
#   # @staticmethod
#   def add(a, b):
#     return a + b
#
# print(MyClass.add(3, 6))

# class MyClass:
#   def __init__(self, first_name, last_name):
#     self.__first_name = first_name
#     self.__last_name = last_name
#
#   # @property
#   def email(self):
#     return "{}.{}@gmail.com".format(self.__first_name,  self.__last_name )
#
# newClass = MyClass("John", "Doe")
#
# print(newClass.email())
# >> TypeError: 'str' object is not callable

# class MyClass(object):
#     count = 0
#
#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1
#
#     def set_val(self, newval):
#         self.val = newval
#
#     def get_val(self):
#         return self.val
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())
#
# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())
#
# print(newClass.email)
# # >> John.Doe@gmail.com

# class MyClass(object):
#     count = 0
#
#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1
#
#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value
#
#
# a = MyClass(5)
# b = MyClass(10)
# c = MyClass(15)
#
# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))

# class PrintList(object):
#
#     def __init__(self, my_list):
#         self.mylist = my_list
#
#     def __repr__(self):
#         return str(self.mylist)
#
#
# printlist = PrintList(["a", "b", "c"])
# print(printlist.__repr__())

#
# from faker import Faker
# fake = Faker()
# print(fake.date())
# from faker import Faker
# fake = Faker()
#
# def create_file(num):
#     f = open("datefile" + num + ".txt", "w")
#     for _ in range(100):
#         f.write(f"{fake.date()}\n")
#     f.close()
# print(fake.date())
#
#
# create_file('1')
# create_file('2')
#
# import sys
# import typing
#
# from tabulate import tabulate
#
# def main(file1, file2):
#     file1_contents = extract_file_contents(file1)
#     file2_contents = extract_file_contents(file2)
#
#     display_files(file1_contents, file2_contents)
#
#     dates = sorted(set(file1_contents).union(file2_contents))
#     print(dates[len(dates) // 2])
#
# def display_files(file1_contents, file2_contents):
#     table = {
#         'file1': file1_contents,
#         'file2': file2_contents
#     }
#     print(tabulate(table))
#
# def extract_file_contents(file_path: str) -> typing.List[str]:
#     """
#     Extract file contents and strip whitespaces from each row.
#     : param file_path: The path to the file to extract
#     : return: A list of date data rows
#     """
#
#     with open(file_path, 'r') as f:
#         file_contents = f.readlines()
#     new_file_contents = []
#     for date_data_record in file_contents:
#         date_data_record = date_data_record.strip()
#         if date_data_record:
#             new_file_contents.append(date_data_record)
#     return new_file_contents
#
# if __name__ == '__main__':
#     args = sys.argv[1:]
#     if len(args) != 2:
#         print(f"Expected two arguments as files. Got {len(args)} instead.")
#         sys.exit(1)
#     main(*args)
# import os
# os.mkdir('day4')
# os.mkdir('day5')
# import time
#
# before = time.time()
# long_number = 1000**1000
# after = time.time()
#
# print(f"It took {after - before} seconds to execute 1000**1000")

# print(abs(7-14))
# print(int('7'))
# print(int(input('input')))

# __doc__ = 'hello'
#
# print(__doc__)

# class Currency:
#     def __init__(self,cur,amount):
#         self.cur = cur
#         self.amount = amount
#
#     def __str__(self):
#         return(f"{self.amount} {self.cur}")
#
#     def __int__(self):
#         return(self.amount)
#
#
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)
#
# print(str(c1))

# print(int(c1))

# >>> repr(c1)
# '5 dollars'
#
# >>> c1 + 5
# 10
#
# >>> c1 + c2
# 15
#
# >>> c1
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars
#
# >>> c1 += c2
# >>> c1
# 20 dollars
#
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

# from datetime import datetime, timedelta, date
#
#
# # def jan():
# #     now = date.today()
# #     j = date(2023, 1, 1)
# #
# #     print(f"the amout of time till january is {j-now}")
# #
# #
# # jan()
#
#
# def birth():
#     y = int(input('birthday: year'))
#     m = int(input('birthday: m'))
#     d = int(input('birthday: d'))
#     now = datetime.now()
#     j = date(y,m,d)
#     print(now)
#     print(f"your alive {now-datetime.timedelta(j)} minutes")
#
#
# birth()

# from datetime import datetime,timedelta
#
# birdthay_input = input("Give my your Birthday in YYYY/MM/DD ")
#
# def birthday(input_value):
#     birth = datetime.strptime(input_value, "%Y/%m/%d")
#     actual_date = datetime.now()
#     minutes_lived = actual_date-birth + timedelta(minutes=0)
#     print(f"You're living since {minutes_lived}")
#
# birthday(birdthay_input)

from time import time

def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"took {t2-t1} ms")
        return result
    return wrapper()


@performance
def long_time():
    for i in range(1000000):
        i*5
