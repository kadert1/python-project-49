from random import randint, choice


DESCRIPT = "What is the result of the expression?"


def generate_round():
    begin_random_num = 1
    end_random_num = 10
    random_num_one = randint(begin_random_num, end_random_num)
    random_num_two = randint(begin_random_num, end_random_num)
    operator = choice('+-*')
    if operator == '+':
        question = f"{random_num_one} + {random_num_two}"
        correct = random_num_one + random_num_two
    if operator == '-':
        question = f"{random_num_one} - {random_num_two}"
        correct = random_num_one - random_num_two
    if operator == '*':
        question = f"{random_num_one} * {random_num_two}"
        correct = random_num_one * random_num_two
    return question, str(correct)
