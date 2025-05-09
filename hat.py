import random

houses = ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]


def sort(name):
    print(name, "is in", random.choice(houses))


sort("harry")
