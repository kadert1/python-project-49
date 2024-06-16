from random import randint

DESCRIPT = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
LENGHT_CORRECT_ANSWER = 2


def logic():
    begin_random_num = 1
    end_random_num = 50
    random_num = randint(begin_random_num, end_random_num)
    result_list = []
    for i in range(1, random_num + 1):
        if random_num % i == 0:
            result_list.append(i)
    if len(result_list) == LENGHT_CORRECT_ANSWER:
        correct = 'yes'
    else:
        correct = 'no'
    question = random_num
    return question, correct
