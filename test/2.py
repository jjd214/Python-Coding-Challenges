import random

keep_playing = "yes"

while keep_playing == "yes":
    magic_number = random.randint(1, 100)

    guess_count = 0

    guess = -1

    while guess != magic_number:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1

        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")

    print(f"It took you {guess_count} guesses")

    keep_playing = input("Would you like to play again (yes/no)? ")

print("Thank you for playing. Goodbye.")