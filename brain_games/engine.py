import prompt


def welcome_user():
    print("Welcome to the Brain Games!")


def name_user():
    return prompt.string("May I have your name? ")


def user_answer():
    return prompt.string("Your answer: ")


def uncorrect(us_answ, result, name):
    print(f"""'{us_answ}' is wrong answer ;(. Correct answer was '{result}'.
Let's try again, {name}!""")
