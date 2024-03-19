#Task 1
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

def check_score(x):
    if x < 80:
          return True  
    else:
          return False
failing = list(filter(check_score, grades))
#failing == 78

student_failing = grades.index(78)

failing_data = students[2], grades[2], activities[2]

print(failing_data)

#Task 2
students_approved = ["John", "Doe", "Smith"]

#Task 3
print(students_approved)