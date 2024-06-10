from ..engine import welcome_user, name_user, user_answer, uncorrect
from random import randint, choice


def brain_calc():
    welcome_user()
    name = name_user()
    print(f"Hello, {name}!")
    operations = ['+', '-', '*']
    count_quest = 0
    winscore = 3
    begin_random = 1
    end_random = 10
    flag = True
    print("What is the result of the expression?")
    while count_quest < winscore:
        one_num = randint(begin_random, end_random)
        two_num = randint(begin_random, end_random)
        random_operations = choice(operations)
        print('Question:', one_num, random_operations, two_num)
        user_ans = user_answer()
        count_quest += 1
        if random_operations == '+':
            answer = str(one_num + two_num)
        if random_operations == '-':
            answer = str(one_num - two_num)
        if random_operations == '*':
            answer = str(one_num * two_num)
        if answer == user_ans:
            print('Correct!')
        else:
            uncorrect(user_ans, answer, name)
            flag = False
            break
    if count_quest == winscore and flag:
        print(f'Congratulations, {name}!')