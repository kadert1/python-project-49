from ..engine import welcome_user, name_user, user_answer, uncorrect
from random import randint
from ..engine import congratulations


def brain_even():
    welcome_user()
    name = name_user()
    print(f"Hello, {name}!")
    count_quest = 0
    begin_num = 1
    end_num = 100
    winscore = 3
    flag = True
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while count_quest < winscore:
        count_quest += 1
        random_num = randint(begin_num, end_num)
        print('Question:', random_num)
        user_ans = user_answer()
        if random_num % 2 == 0 and user_ans != 'yes':
            uncorrect(user_ans, 'yes', name)
            flag = False
            break
        elif random_num % 2 != 0 and user_ans != 'no':
            uncorrect(user_ans, 'no', name)
            flag = False
            break
        else:
            print('Correct!')
    congratulations(count_quest, winscore, flag, name)
