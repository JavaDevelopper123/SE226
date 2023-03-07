name = input("What is your name?")

lab_grade = int(input("Lab: "))
midterm_grade = int(input("Midterm: "))
final_grade = int(input("Final: "))

last_score = str(lab_grade * 0.25 + midterm_grade * 0.35 + final_grade * 0.4)

print("Last Score: " + last_score)
