from random import randint


DESCRIPT = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def logic():
    begin_random_num = 1
    end_random_num = 10
    random_num = randint(begin_random_num, end_random_num)
    question = f'{random_num}'
    if random_num % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    return question, correct
