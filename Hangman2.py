#Bye
guessthisword = "hello world"
guessthisword = guessthisword.lower()
correctword = []
wordsguessed = ""
for letters in guessthisword:
    correctword.append(letters)
guesses = []
for letters in correctword:
    if letters == " ":
        guesses.append(" ")
    else:
        guesses.append("_")
word = "".join(guesses)
print(word)
guessesleft = 10
while True:
    userGuess = input("What is your guess: ")
    if userGuess not in wordsguessed:
        if userGuess.lower() in correctword:
            loop = 0
            for letters in correctword:
                if userGuess == letters:
                    guesses[loop] = correctword[loop]
                loop += 1
        else:
            guessesleft -= 1
            print(f"The letter {userGuess} is not in the word")
            print(f"You have {guessesleft} guesses left")
        wordsguessed += userGuess
    else:
        print("You already guessed that word")
    word = "".join(guesses)
    print(word)
    if guesses == correctword:
        print("You guessed the word")
        break
    if guessesleft == 0:
        print("You have ran out of guesses")
        break
