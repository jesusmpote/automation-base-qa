import datetime
from random import random


def generate_random_number():
    return str(datetime.datetime.now().timestamp()).replace(".", "")


def generate_random_other_number():
    return str(random()).replace(".", "")

numero = print(generate_random_other_number())

