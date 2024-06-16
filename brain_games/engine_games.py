import prompt


WINSCORE = 3


def engine(game):
    count_round = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPT)
    while count_round < WINSCORE:
        count_round += 1
        question, correc = game.logic()
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        if ans != correc:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{correc}'.")
            print(f"Let's try again, {name}!")
            count_round = 10
            break
        print('Correct!')
    if count_round == WINSCORE:
        print(f"Congratulations, {name}!")
