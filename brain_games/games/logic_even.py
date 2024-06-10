from ..engine import welcome_user, name_user, user_answer, uncorrect
from random import randint


def brain_even():
    welcome_user()
    name = name_user()
    print(f"Hello, {name}!")
    count_quest = 0
    begin_num = 1
    end_num = 100
    winscore = 3
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while count_quest < winscore:
        count_quest += 1
        random_num = randint(begin_num, end_num)
        print('Question:', random_num)
        user_ans = user_answer()
        flag = True
        if random_num % 2 == 0:
            if user_ans == 'yes':
                print('Correct!')
            else:
                uncorrect(user_ans, 'yes', name)
                break
        if random_num % 2 != 0:
            if user_ans == 'no':
                print('Correct!')
            else:
                flag = False
                uncorrect(user_ans, 'no', name)
                break
    if count_quest == winscore and flag is True:
        print(f"Congratulations, {name}!")
