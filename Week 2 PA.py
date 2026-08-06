correctNumber = 5
numberOfTries = 0

userName = input("What is your name? ")
studentID = input("What is your student ID? ")

userGuess = int(input("Please guess a number between 1 and 10: "))
numberOfTries += 1

while userGuess != correctNumber:
    if userGuess < correctNumber:
        print("You guessed too low.")
    else:
        print("You guessed too high.")


    userGuess = int(input("Please guess a number between 1 and 10: "))
    numberOfTries += 1

print("Congratulations,", userName + "!")
print("You guessed the number in", numberOfTries, "tries!")

print()
print("Output from the 'while' loop:")

counter = 1

while counter <= 5:
    incrementedNumber = correctNumber + counter
    print(correctNumber, "incremented by", counter, "is", incrementedNumber)
    counter += 1

print()
print("Output from the 'for' loop:")

for counter in range(1, 6):
    incrementedNumber = correctNumber + counter
    print(correctNumber, "incremented by", counter, "is", incrementedNumber)
