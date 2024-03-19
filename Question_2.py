#Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

on_time_in_person = list(set(submitted).intersection(attended))

print(on_time_in_person)

#Task 2
matching = ["identical" if "Charlie" and "Eve" and "Alice" and "Frank" in submitted else print("not identical")]

print(matching)

#Task 3
missing_assignment = [attended.remove(x) if x not in submitted else x for x in attended]

print(missing_assignment)