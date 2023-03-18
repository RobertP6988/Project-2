"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Robert Pešek
email: robert.pesek@email.cz
discord: Robert P.#6988
"""

import random
import time
import os

os.system('cls')

start_time = time.perf_counter()

# pravidla:
# bull = číslo na stejné pozici
# cow = číslo v rětězci, ale na jiné pozici

# pomocné proměnné 1
gap = "-" * 47
runs = 0

# genrování náhodného čísla počítačem
limit = range(1, 10)
number_pc = list(map(str, random.sample(limit, 4)))
# print(number_pc)
print(type(limit))

# přivítání
print(
    """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------"""
)

# zadání čísla uživatelem
while True:
    my_number = input("Enter a number:")
    print(">>>", my_number)

    # pokud je zadáno q hra se ukončí
    if my_number == "q":
        print("Game stopped :-(")
        break

    # podmínka pro zadání akceptovatelného čísla a počítání pokusů
    # pozn. nepočítá zadání ve špatném formátu
    elif (
        not my_number.isdigit()
        or not len(my_number) == 4
        or not len(set(my_number)) == 4
        or my_number[0] == "0"
    ):
        print(
            """Wrong format, please enter 4 digit number consist of unique numbers or enter "q" to end a game"""
        )
        print(gap)
    else:
        my_number = list(my_number)
        runs += 1

        # pomocné proměnné 2
        bulls = 0
        cows = 0

        # výpis počtu pokusů a času hry
        if my_number == number_pc:
            print("Correct, you've guessed the right number in", runs, "guesses!")
            end_time = time.perf_counter()
            run_time = round(end_time - start_time, 2)
            print("Game run", run_time, "second")
            print(gap)

            # výpis hodnocení výkonu podle zadaných limitů
            print("That", end="")
            if run_time < 20:
                print("´s amazing")
            elif run_time < 40:
                print("´s good")
            elif run_time < 60:
                print("´s average")
            elif run_time < 90:
                print("´s not so good")
            else:
                print(" should be improved a little :) ")
            break

        # porovnání přítomnosti čísla a pozic
        for pozice, split_pc in enumerate(number_pc):
            if split_pc in my_number:
                cows += 1
                if split_pc == my_number[pozice]:
                    cows -= 1
                    bulls += 1

        # výpis počtu "cows" and "bulls"
        if bulls>1:
            print(bulls, "bulls,",end=' ')
        else: print(bulls, "bull,",end=' ')
        if cows>1:
            print(cows, "cows")
        else: print(cows, "cow")
        print(gap)
