# A game to guess the 3 digit unique code that computer has generated
# whenever we guess, computer will give clues as follows:
# if a number matches at the right position : match
# if a number is in the code but wrong position in the guess : close
# if none of the numbers is in the guess : none
# it should repeatedly ask until the user has guessed the number or quit

from random import randint


def generate_code():
    unique_code = set()
    codestr = ""
    while True:
        unique_code.add(randint(1, 9))
        if len(unique_code) == 3:
            break
    for i in unique_code:
        codestr += str(i)
    return codestr


def match(guess):
    for i in guess:
        if i in code:
            if guess.index(i) == code.index(i):
                return guess
    return ""


def close(guess):
    for i in guess:
        if i in code:
            return guess
    return ""


def start_game():
    print(f"Welcome to crack the code game\nCode has been generated")

    while True:
        print("What is your guess")
        code_guess = input()
        if code_guess == code:
            print("Code Cracked")
            break
        elif code_guess == match(code_guess):
            print("match")
        elif code_guess == close(code_guess):
            print("close")
        else:
            print("none")


code = generate_code()
start_game()
