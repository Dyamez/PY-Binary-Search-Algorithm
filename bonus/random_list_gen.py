import random

def make_random_list(size = 10, min =- 100, max = 100):
    return [random.randint(min, max) for n in range(size)]