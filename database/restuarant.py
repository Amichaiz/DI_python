from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['menu']
col = db['menu']


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.query = {"price": self.price, "name": self.name}

    def save(self):
        return col.insert_one(self.query)

    def delete(self):
        return col.delete_one(self.query)

    def update(self, newprice, newname):
        return col.update_one(self.query, {"$set": {"price": newprice, "name": newname}})

    @staticmethod
    def all():
        return col.find({})

    @staticmethod
    def get_by_name(search):
        if col.find({"name": search}).count() > 0:
            return col.find({"name": search})
        else:
            return 'none'


item = MenuItem('Burger', 35)
# print(item.save())
# item.delete()
item.update('Veggie Burger', 37)
items = MenuItem.all()
# for x in items:
print(item2)
