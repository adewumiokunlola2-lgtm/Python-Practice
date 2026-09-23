try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That wasn't a valid number")

try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
except ValueError as ex:
    print("Exception", ex)