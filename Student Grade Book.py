grades = {"Alice": 85, "Bob": 89, "Charlie": 94, "David": 76, "Eve": 97}
print(grades)

total = 0

for i in grades.values():
    total = total + i

print("Total scores:", total)

average = total / len(grades)
print("Average:", average)

highest_score = max(grades)
print("Highest score:", highest_score)

lowest_score = min(grades)
print("Lowest score:", lowest_score)

student_name = input("Enter a student's name: ")


for i in grades:
    if student_name == i:
        print(grades[i])
    else:
        print("This student does not exist.")
        exit()