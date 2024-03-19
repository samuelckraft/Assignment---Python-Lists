#Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()

print(grades)

#Task 2
avg = sum(grades) / len(grades)

print(avg)

#Task 3
failed = ["Fail" if x < 80 else x for x in grades]

print(failed)

