# import mysql.connector
# from mysql.connector import errorcode
#
# try:
#     cnx = mysql.connector.connect(
#         host="109.64.6.128",
#         user="pbadmin_py",
#         password="oB])xdE[!^SS",
#         database="pbadmin_dev_pb"
#     )
#     mycursor = cnx.cursor()
#
#     sql = "INSERT INTO colors (colorName, last_user) VALUES (%s, %s)"
#     val = ("hello", "35")
#     mycursor.execute(sql, val)
#
#     cnx.commit()
#
#     print(mycursor.rowcount, "record inserted.")
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#     cnx.close()


# user = 'amiz'
# password = 'YKA3Oxd5215XAydj'

from pymongo import MongoClient
import pymongo
# pprint library is used to make the output look more pretty
# from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://localhost:27017')
# Issue the serverStatus command and print the results
mydb = client['myfirstdb']
mycol = mydb['users']
mydict = { "name": "John", "address": "Highway 37" }

# for x in mycol.find():
#   print(x)

# for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
#   print(x)

# for x in mycol.find({},{ "address": 0 }):
#   print(x)

myquery = { "id": 1 }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)