day = input("Enter the day of the week: ")
if day in ("Saturday" , "Sunday"):
     print("Day type: Weekend - enjoy your free time!")
elif day == "Monday":
     print("Day type: First day of the week.")
elif day == "Friday":
     print("Day type: Last school day.")
elif day in ("Tuesday" , "Wednesday" , "Thursday"):
     print("Day type: Regular school day.")
else:
     print("Day not recognised.")


weather = input("Enter the weather today (sunny, rainy, cloudy):  ")
homework = input("Is your homework done? (yes/no):  ")
if weather == "sunny" and homework == "yes":
     print("After school: Head to the park!")


if weather == "rainy" or weather ==  "cloudy":
     print("Weather tip: Pack your umbrella!")

if not (homework == "yes"):
          print("Homework: Not done yet. Finish it before going out!")
if day != "Saturday":
        print("It is a school week day")