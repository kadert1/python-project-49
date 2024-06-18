from random import randint


DESCRIPT = "What number is missing in the progression?"
LENGHT_PROGRESSION = 10


def generate_round():
    begin_random_num = 1
    end_random_num = 20
    begin_step = 1
    end_step = 10
    start_progression = randint(begin_random_num, end_random_num)
    step_progression = randint(begin_step, end_step)
    random_question = randint(0, LENGHT_PROGRESSION - 1)
    progression = [start_progression]
    for i in range(LENGHT_PROGRESSION):
        progression.append(progression[i] + step_progression)
    correct = progression[random_question]
    progression[random_question] = '..'
    question = list(map(str, progression))
    return ' '.join(question), str(correct)
