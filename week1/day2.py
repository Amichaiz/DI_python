# my_fav_numbers = {3,10}
# #print(my_fav_numbers)
# my_fav_numbers.remove(10)
# #print(my_fav_numbers)
# friend_fav_numbers = {34,24,45}
# defd = my_fav_numbers.union(friend_fav_numbers)
# #print(defd)
# # 2 no its imutable
# #for i in range(20):
# #    print(i)
#
# list = []
# for i in range(10, 50, 5):
#     list.append(i/10)
# print(list)
#
# max = 0
# #for i in range(3):
# #    x = int(input("number please"))
# #    if x > max:
# #        max = x
# #print(f"the biggest num is {max}")
#
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# x = input("name please")
# #if x in names:
#     #print(names.index(x))
#
# import random
# n = random.randint(0, 10)
# print(f"sd {n}n")
#
# x = input("birthday please")

#
# list = [1, 2, 3, 4, 5, 6, 6, 7]
# print(len(list))
# list.append(100)
# list.insert(2, 100)
# list.extend([200])
# list.pop(0)
# list.remove(200)
# list.clear()
# print(list)
# new_list = list[:]
# new_list[0]=10
# print(new_list)
# print(list)

# print(list(range(1,100)))
bask = ['a', 'b', 'c', 'd', 'e', 'c']
bask.sort()
print(bask.index('b'))
print(bask.count('d'))
print(list(range(10)))

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is {i}")

