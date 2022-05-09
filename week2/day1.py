class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


rino1 = Cat('rino1', 23)
rino2 = Cat('rino2', 220)
rino3 = Cat('rino3', 1500)


def oldest(*cats):
    old = cats[0]
    for cat in cats:
        if old.age < cat.age:
            old = cat
    return old.age


print(f"The oldest cat is {oldest(rino1, rino2, rino3)} years old.")


class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high")


davids_dog = Dog('rex', 50)
sarahs_dog = Dog('Teacup', 20)
print(davids_dog.bark())
print(davids_dog.jump())
print(sarahs_dog.bark())
print(sarahs_dog.jump())


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


class Farm:
    def __init__(self, name):
        self.name = name
        self.zoo = {}

    def add_animal(self, animal, amount=1):
        #print(self.zoo[animal])
        #if self.zoo[animal] > 1:
        #    self.zoo[animal] = self.zoo[animal]+amount
        #else:
        self.zoo[animal] = amount

    def get_info(self):
        print(f'''
        {self.name}'s farm

{self.zoo}

    E-I-E-I-0!''')


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()

