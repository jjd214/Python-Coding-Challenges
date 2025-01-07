import random

def main():

    play = True

    while(play):

        magic_number = random.randint(1,100)
        temp_num = -1
        count = 0

        while magic_number != temp_num:
            guess = int(input("What is your guess? "))
            count+=1
            if guess == magic_number:
                print("You guessed it!")
                print(f"It took you {count} guesses")
                break

            elif guess > magic_number:
                print("Lower")

            elif guess < magic_number:
                print("Higher")

        again = input("Would you like to play again (yes/no)? ").lower()

        if again == 'no':
            print("Thank you for playing. Goodbye.")
            play = False

main()
