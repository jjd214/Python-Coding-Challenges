def main():
    secret_word = "mice"
    count = 0
    print("Welcome to the word guessing game!")
    print(f"Hint: {len(secret_word)} letters")

    while True:
        guess = input("What is your guess? ").lower()
        count += 1
        hint = ""

        if guess == secret_word:
            print("You guessed it right!")
            print(f"It took you {count} guesses")
            break

        for i, char in enumerate(guess):
            if i < len(secret_word) and char == secret_word[i]:
                hint += char.upper() + " "
            elif char in secret_word:
                hint += char + " "
            else:
                hint += "_ "

        print(f"Your hint is {hint}")

main()
