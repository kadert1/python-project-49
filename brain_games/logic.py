import prompt
from random import randint


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    count_quest = 0
    begin_num = 1
    end_num = 100
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while count_quest < 3:
        random_num = randint(begin_num, end_num)
        print('Question:', random_num)
        answer = prompt.string("Your answer: ")
        if random_num % 2 == 0 and answer != 'yes':
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
            count_quest = 10
        elif random_num % 2 != 0 and answer != 'no':
            print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
            count_quest = 10
        else:
            print('Correct!')
            count_quest += 1
    if count_quest == 3:
        print(f"Congratulations, {name}!")
