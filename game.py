"""Guessing Game: the computer guesses the number chosen by the player."""

def main():
    print("Think of a whole number between 1 and 100.")
    input("Press Enter when you are ready...")

    low = 1
    high = 100
    guesses = 0

    while low <= high:
        guess = (low + high) // 2
        guesses += 1

        print(f"My guess is {guess}.")
        response = input("Is it (h)igher, (l)ower, or (c)orrect? ").strip().lower()

        if response == "c":
            print(f"I guessed your number in {guesses} guesses!")
            return
        elif response == "h":
            low = guess + 1
        elif response == "l":
            high = guess - 1
        else:
            print("Please enter h, l, or c.")

    print("Your answers were inconsistent, so I could not determine the number.")

if __name__ == "__main__":
    main()
