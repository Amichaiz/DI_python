# sample_dict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sample_dict['class']['student']['marks']['history'])
# print(sample_dict.items())

# y67hn
#
# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }
#
# for x, y in my_books.items():

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict1 = zip(keys,values)
#
# print(dict(dict1))

# users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
# print(sorted(users))
# dic = {}
# dict = {}
# for i,user in enumerate(users):
#     dic[user]=i
# print(dic)
# for i,user in enumerate(users):
#     dict[i]=user
# print(dict)

# ite= {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }
#
# for fruit, price in ite.items():
#     print(f"The price of {fruit} is {price}")
#
# for fruit, price in ite.items():
#     ite[fruit] = {"price": price,
#                     "quantity": 4}
#
# print(ite)
# total_cost = sum([priceQuantityPair["price"]*priceQuantityPair["quantity"] for priceQuantityPair in ite.values()])
# print(total_cost)

# x = int(input('number'))
# sum = 0
# for num in range(1, x):
#     if x % num == 0:
#         sum += num
# if sum == x:
#     print('true')
# else:
#     print('false')

# string = input('text')
# temp = string.split()
# temp.reverse()
# print(' '.join(temp))

# my_list = [char for char in 'hello']
# my_list1 = [num for num in range(100)]
# my_list2 = [num*2 for num in range(100)]
# my_list3 = [num**2 for num in range(100) if num % 2 == 0]
#
# print(my_list3)

# list_1 = ['a', 'b', 'b', 'c', 'c']
# dup = [x for x in list_1 if list_1.count(x) > 1]
# print(list(set(dup)))

user = {
    'ami': [1, 2, 3],
    'tami': 'hello'
}
print(user.get('as',23))
