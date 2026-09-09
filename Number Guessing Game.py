secret = 35
attempts = 0
won = False

while attempts < 5 and won == False:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts = attempts + 1

    if guess == secret:
        print("You win!")
        won = True

    else:
        difference = abs(secret - guess)

        if difference <= 5:
            print("Hot!")
        elif difference <= 10:
            print("Warm!")
        elif difference <= 20:
            print("Cold!")
        else:
            print("Ice cold!")

        print("Remaining lives: ", end="")

        for i in range(5 - attempts):
            print("❤️", end="")

        print()

if won == False:
    print("You lose! The secret number was", secret)