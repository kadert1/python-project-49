from random import randint
from ..engine import welcome_user, name_user, user_answer, uncorrect
from ..engine import congratulations


def brain_progression():
    welcome_user()
    name = name_user()
    flag = True
    begin_random = 1
    end_random = 10
    begin_step_random = 1
    end_step_random = 5
    winscore = 3
    length_progression = 10
    print(f"Hello, {name}!")
    count_quest = 0
    print("What number is missing in the progression?")
    while count_quest < winscore:
        count_quest += 1
        quest_numbers = []
        begin_progression = randint(begin_random, end_random)
        step = randint(begin_step_random, end_step_random)
        while len(quest_numbers) <= length_progression:
            for i in range(begin_progression, 100, step):
                quest_numbers.append(i)
        copy_numbers = quest_numbers[:]
        random_index = randint(0, 9)
        quest_numbers[random_index] = '..'
        correct_answer = copy_numbers[random_index]
        question = ' '.join(map(str, quest_numbers[0:10]))
        print('Question:', question)
        user_answ = user_answer()
        if user_answ == str(correct_answer):
            print('Correct!')
        else:
            flag = False
            uncorrect(user_answ, correct_answer, name)
            break
    congratulations(count_quest, winscore, flag, name)
