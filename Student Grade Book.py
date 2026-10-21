student_dict = {"Josh": 85, "Katie": 89, "Naomi": 94, "Layla": 76, "Nathan": 97}

total = 0

for i in student_dict.values():
    total = total + i

print(total)

average = total / len(student_dict)
print(average)

highest_score = max(student_dict)
print(highest_score)

lowest_score = min(student_dict)
print(lowest_score)

student_name = input("Enter a student's name: ")

for i in student_dict:
    if student_name == i:
        print(student_dict[i])
    else:
        print("This student does not exist.")
        exit()