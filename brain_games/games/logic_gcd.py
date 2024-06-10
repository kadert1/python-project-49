from math import gcd
from random import randint
from ..engine import welcome_user, name_user, user_answer, uncorrect


def brain_gcd():
    welcome_user()
    name = name_user()
    flag = True
    print(f"Hello, {name}!")
    count_quest = 0
    winscore = 3
    begin_random = 1
    end_random = 10
    print("Find the greatest common divisor of given numbers.")
    while count_quest < winscore:
        count_quest += 1
        num_1 = randint(begin_random, end_random)
        num_2 = randint(begin_random, end_random)
        print('Question:', num_1, num_2)
        user_ans = user_answer()
        result = gcd(num_1, num_2)
        if str(result) == user_ans:
            print('Correct!')
        else:
            flag = False
            uncorrect(user_ans, result, name)
            break
    if count_quest == winscore and flag is True:
        print(f"Congratulations, {name}!")
