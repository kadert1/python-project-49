from random import randint
from math import gcd


DESCRIPT = "Find the greatest common divisor of given numbers."


def logic():
    begin_random_num = 1
    end_random_num = 10
    random_num_one = randint(begin_random_num, end_random_num)
    random_num_two = randint(begin_random_num, end_random_num)
    question = f"{random_num_one} {random_num_two}"
    correct = gcd(random_num_one, random_num_two)
    return question, str(correct)
