from random import randint
from ..engine import welcome_user, name_user, user_answer, uncorrect
from ..engine import congratulations


def brain_prime():
    welcome_user()
    name = name_user()
    begin_random = 1
    end_random = 20
    winscore = 3
    count_quest = 0
    flag = True
    print(f"Hello, {name}!")
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    while count_quest < winscore:
        count_quest += 1
        question = randint(begin_random, end_random)
        print('Question:', question)
        user_ans = user_answer()
        result_list = []
        for i in range(1, question + 1):
            if question % i == 0:
                result_list.append(i)
        if len(result_list) == 2 and user_ans != 'yes':
            uncorrect(user_ans, 'yes', name)
            flag = False
            break
        elif len(result_list) != 2 and user_ans != 'no':
            uncorrect(user_ans, 'no', name)
            flag = False
            break
        else:
            print('Correct!')
    congratulations(count_quest, winscore, flag, name)
