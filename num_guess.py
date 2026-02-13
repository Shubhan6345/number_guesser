import random
import time

print("""
                            WELCOME TO NUMBER GUESSER
    
    You must guess the number im thinking of. You have 3 difficulty levels ->
        
        1. EASY : 10 guesses
        2. MEDIUM: 7 guesses
        3. HARD: 5 guesses
      
""")

hs = 0
best_time = 0

while True: 

    gcount = 0
    num = random.randint(1,100)
    difficulty = int(input("\nChoose 1, 2, or 3: ").strip())

    if difficulty == 1:
        guesses = 10
    elif difficulty == 2:
        guesses = 7
    else:
        guesses = 5

    start = time.perf_counter()

    # game logic

    for x in range(guesses):

        gcount += 1
        g = int(input("\nEnter guess: "))

        if g > num:
            print(f"Incorrect! {g} is HIGHER than the number.")
        elif g < num:
            print(f"Incorrect! {g} is LOWER than the number.")
        else:
            print("\nCORRECT!!")
            break
    else:
        print(f"\nYOU LOST! The correct number was {num}.")

    # time elapsed

    end = time.perf_counter()
    elap = end-start
    print(f"\nYou took {elap:.2f} seconds to complete the game!")

    # high score counter

    if hs == 0 or gcount < hs:
        hs = gcount
        print(f"\nYour new lowest score yet is {hs}!")
    else:
        print(f"\nYour took {gcount} guess(es) to complete the game!")

    # continue game

    pa = input("\nWould you like to play again? (Y/N) : ").strip().lower()

    if pa == "y":
        continue
    else:
        break