import random

"""
This simple game generates random number (from 1 to 100), takes input from user (integer)
and compares with generated random number. If number is too small or too big informs the user and continue guess.
When the numbers are the same YOU WIN !
Program ends.

"""
comp_num = random.randint(1, 100)


def guess(user: int) -> None:
    try:
        print("Welcome! Try to guess the number from 1 to 100, good luck!")
        while True:
            user = int(input("Guess the number: "))
            if user < comp_num:
                print("It's too small!")
            elif user > comp_num:
                print("It's too big!")
            else:
                print("You win!")
                return
    except ValueError:
        print("It's not a number")


guess(comp_num)
