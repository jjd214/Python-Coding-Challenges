import random

while input("Play? (yes/no): ").lower() == "yes":
    magic_number = random.randint(1, 100)
    guess_count = 0

    while (guess := int(input("Your guess: "))) != magic_number:
        print("Higher" if guess < magic_number else "Lower")
        guess_count += 1

    print(f"You guessed it in {guess_count + 1} tries!")
print("Goodbye!")
