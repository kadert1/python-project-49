from random import randint

DESCRIPT = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
LENGHT_CORRECT_ANSWER = 2


def is_prime(number):
    result_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            result_list.append(i)
    if len(result_list) == LENGHT_CORRECT_ANSWER:
        return True
    return False


def generate_round():
    begin_random_num = 1
    end_random_num = 50
    random_num = randint(begin_random_num, end_random_num)
    question = random_num
    correct = 'no'
    if is_prime(random_num):
        correct = 'yes'
    return question, correct
