class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = Parrot("blue---", 60)
woo = Parrot("woo----", 10)

print("Blu is a {} ".format(blu.__class__.species))
print("woo is a {} ".format(woo.__class__.species))

print("{} is a {} ".format(blu.name, blu.age))
print("{} is a  {}".format(woo.name, woo.age))
