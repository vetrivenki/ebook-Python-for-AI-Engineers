secret_number = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == secret_number:
        print("Correct!")
        break

    attempts -= 1
    print(f"Incorrect. Attempts left: {attempts}")
else:
    print(f"The number was {secret_number}")
