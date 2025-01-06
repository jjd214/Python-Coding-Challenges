secret_word = "mouse"
ctr = 0

print("\nWelcome to the word guessing game!\n")

underscore = ""
for x in range(len(secret_word)):
    underscore += "_ "
print(f"Hint: {len(secret_word)} letters")

while True:
    user_guess = input("What is your guess? ").lower()
    ctr += 1
    
    if user_guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {ctr} guesses.")
        break
    else:
        r = ""
        for x in range(len(user_guess)):
            flag = False
            ilan = secret_word.count(user_guess[x])
            if ilan > 0:
                for y in range(len(secret_word)):
                    if x == y and user_guess[x] == secret_word[y]:
                        r += user_guess[x].upper() + " "
                        flag = False
                        break
                    elif user_guess[x] == secret_word[y]:
                        flag = True
            else:
                r += "_ "
            
            if flag:
                r += user_guess[x] + " "

        print(f"Your hint is {r}")