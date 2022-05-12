# f = open('secrets.txt')
# secret_data = f.read()
# # secret_data is a string
#
# f.close()

# f = open('secrets.txt', 'w+')
# f.write('This is a new line')
# print(f)

# f = open('secrets.txt','a+')
# f.write('\nThis is text being appended to test.txt')
# f.write('\nAnd another line here.')
# f.close()

# try:
#    f = open("secrets.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()

# with open('output.txt', 'w') as f:
#     for i in range(10):
#        f.write("this is line: %i\n"%i)
# for line in open('secrets.txt'):
#     print(line)
# ----------------json--------------
# import json
#
# my_family = {
#     "parents":['Beth', 'Jerry'],
#     "children":['Summer', 'Morty']
# }
#
# json_file = "my_file.json"
#
# with open(json_file, 'w') as file_obj:
#     json.dump(my_family, file_obj)
#    #json.dump(obj2save , destination_file)

# import json
#
# json_file = 'my_file.json'
# with open(json_file, 'r') as file_obj:
#     my_family = json.load(file_obj)
#
# print(my_family)
import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.headers)
#
# parameters = {"lat": 31.771959, "lon": 35.217018}
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# print(response.text)

# response = requests.get("https://api.chucknorris.io/jokes/random")
#
# # Print the content of the response (the data the server returned)
# # data = response.json()['value']
#
# print(data)

from random import choice


# def get_words_from_file(file):
#     with open(file) as f:
#         word_list = f.readlines()
#         word_list = [word.replace("\n", "") for word in word_list]
#         return word_list
#
#
# def get_random_sentence(word_list, num):
#     new_sentence = []
#     for word in range(num):
#         new_sentence.append(choice(word_list).title())
#     return " ".join(new_sentence)
#
#
# def main():
#     print("This program takes your chosen length between 2-20 and generates a random sentence")
#     num = int(input("Please enter the length: "))
#     if 2 <= num <= 20:
#         text = get_words_from_file("secrets.txt")
#         print(get_random_sentence(text, num))
#     else:
#         raise ValueError
#
#
# main()
#
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# print(sampleJson.json())


class Text:
    def __init__(self, text):
        self.text = text

    def freq(self, word):
        return self.text.split(" ").count(word) if self.text.split(" ").count(word) > 0 else None

    def common(self):
        text_set = list(set(self.text.split(" ")))
        highest = text_set.pop(0)
        for word in text_set:
            if self.text.split(" ").count(word) > self.text.split(" ").count(highest):
                highest = word
        return highest