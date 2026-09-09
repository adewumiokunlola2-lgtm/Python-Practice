secret = 27

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50!")
print("You only have 5 attempts to guess the correct number!")
print("Guess wisely! Good luck!")

guess = int(input("Enter a number: "))

while guess != secret:
    if guess < secret:
        print("Your guess is too low. Try again!")
        break
    elif guess > secret:
        print("Your guess is too high. Try again!")
        break
else:
    print("Congratulations! You guessed the correct number!")
    
