# a = ["b", "g", "a", "d", "f", "c", "h", "e"]
# x = sorted(a)
# print("a after sorted function")
# print(a)
# print(x)
# b = [1, 2, 5, 8, 3]
# b.sort()
# print(b)

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst[0:4])
# print(lst[::])
# print(lst[::-1])

# t = (1, 2, 3, 4, 5, "a", "b", "c")
# t1 = 1, 2, 3, 4, "g", "l"
# print(t)
# print(t1)
# print(len(t))

# d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# l1 =list(d.keys())
# print("the key values are:")
# print(l1)
# l2 = list(d.values())
# print("The values are of dictionary is")
# print(l2)
# l3 = list(d.items())
# print("the list items are")
# print(l3)

# a = {1, 2, 3, 4, 5}
# b = {2, 3, 6, 7, 5}
# c = a^b
# print(c)
# d = a - b
# print(d)
# e = b - a
# print(e)

# A squaring lambda function
# square = lambda n : n*n
# num = square(5)
# print(num)

# sub = lambda x, y : x-y
# print(sub(5, 3))

# def say_hello():
#     """A function  ewijo
#     ds
#      efwf
#      that says hello"""
#     print("Hello!")
#
#
# say_hello()

# def calculation(a, b):
#     return a+b, a-b
#
#
# res = calculation(40, 10)
# print(res)

# def my_f1():
#     print("Hello")
#
#
# def my_f2():
#     print("Word")
#
#
# def my_f3():
#     print("This is Rick!")
#
#
# list_of_functions = [my_f1, my_f2, my_f3]
# for function in list_of_functions:
#     print(function())

# def check_arguments(*args):
#     print(f"These are the arguments {args}")
# check_arguments(1, 2, 'hey')
# def th(peopl):
#     return len(peopl) == 4
#
#
# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# map_object = filter(th, people)
#
# print(list(map_object))

# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
#
#
# favorite_book('fd')

# def describe_city(city='jlem', country='il'):
#     print(f" {city} is in  {country}")
#
#
# describe_city()

# import random
# n = random.randint(0, 100)
# l = int(input('num to 100'))
# if l == n:
#     print('yat')
# else:
#     print(f'nay {l,n}')

# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
# def numb(num):
#     x = str(num)
#     print(int(x)+int(x*2)+int(x*3)+int(x*4))
# numb(3)

# s = input("String: ")
# ch = input("Character: ")
# #{Write your code here
# print(s.count(ch))

def fd(arr):
    x = len(max(arr, key=len))
    print('*' * (x + 4))
    for i, user in enumerate(arr):
        t = ' ' * (x - len(user))
        print(f'* {user}{t} *')


# fd(["Hello", "World", "in", "reallylongword", "a", "frame"])

# def insertion_sort(alist):
#    for index in range(1,len(alist)):
#
#      currentvalue = alist[index]
#      position = index
#
#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1
#
#      alist[position]=currentvalue
#
# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

# def high(list):
#     def even(param):
#         return param % 2 == 0
#     temp = filter(even, list)
#     return max(temp)
#
#
# print(high([10,15,17,23,24,35]))

matrix = [
    [7, 'i', 3],
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', '', '#'],
    ['', 's', 'M'],
    ['', '$', 'a'],
    ['#', 't', '%'],
    ['^', 'r', '!'],
]
string = ''
for list in matrix:
    if isinstance(list[0], str):
        string += list[0]
print(string)
