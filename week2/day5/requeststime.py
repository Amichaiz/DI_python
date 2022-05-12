import requests
import datetime

a = datetime.datetime.now()
requests.get('https://www.programiz.com/python-programming/time')
requests.get('https://www.imdb.com/')
requests.get('https://www.google.com/')

print(datetime.datetime.now() - a)
