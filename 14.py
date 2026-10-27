import pickle
import shelve

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll number:", self.roll_no)
        print("Marks:", self.marks)


student = Student("Raman", 101, 85)

# Save and restore using pickle
with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

with open("student.pkl", "rb") as file:
    restored = pickle.load(file)

print("Restored using pickle:")
restored.display()

# Save and restore using shelve
with shelve.open("student_data") as database:
    database["student"] = student

with shelve.open("student_data") as database:
    restored_student = database["student"]

print("\nRestored using shelve:")
restored_student.display()