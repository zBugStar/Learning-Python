guess = 0
while guess != 6:
    guess = int(input("Guess the number: "))
    if guess != 6:
        print("Incorrect guess. Try again.")
    else:
        print("Correct guess!")