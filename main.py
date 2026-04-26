#1. CREATE A LIST OF DICTIONARIES WITH STUDENT INFO
#2.CREATE THE FUNCTIONS THAT WILL PERFORM THE DIFFERENT Tasks
#3. Within the functions, there has to be a way the functions are able to access the student system
# and perform their tasks, with the required concepts

#1. LIST OF DICTIONARIES

student_database = [
    {"name": "Lisa", "age": 26, "course": "Law", "marks": 76.5}, {"name": "Lebo", "age": 22, "course": "Acturial Science", "marks": 82.3},
    {"name": "Tom", "age": 24, "course": "Culinary", "marks": 65.5}, {"name": "Amogelang", "age": 23, "course": "Business Studies", "marks": 79.2},
    {"name": "Sam", "age": 19, "course": "Civil Engineering", "marks": 83.8}, {"name": "Hannah", "age": 25, "course": "Psychology", "marks": 57.9},
    {"name": "Kabelo", "age": 22, "course": "Mechanical Engineering", "marks": 67.9}, {"name": "Marina", "age": 24, "course": "Nursing", "marks": 70.9},
    {"name": "Lincoln", "age": 21, "course": "Accounting", "marks": 65.5}, {"name": "Atlegang", "age": 28, "course": "Agriculture", "marks": 68.7},
    {"name": "Joseph", "age": 29, "course": "Architecture", "marks": 55.8}, {"name": "Anna", "age": 22, "course": "Music", "marks": 56.8},
    {"name": "Katlego", "age": 19, "course": "Marketing", "marks": 63.3}, {"name": "Holden", "age": 21, "course": "Law", "marks": 65.3},
    {"name": "Bontle", "age": 22, "course": "Computer Science", "marks": 56.5}, {"name": "Kieth", "age":30, "course": "Mechanical Engineering", "marks": 80.5},
    {"name": "Londiwe", "age": 27, "course": "Computer Science", "marks": 72.1}, {"name": "Peter", "age": 32, "course": "Architecture", "marks": 76.5},
    {"name": "Kyle", "age": 23, "course": "Civil Engineering", "marks": 52.2}, {"name": "Andile", "age": 28, "course": "Culinary", "marks": 86.3},
    {"name": "Palesa", "age": 25, "course": "Accounting", "marks": 46.5}, {"name": "Heather", "age": 19, "course": "Marketing", "marks": 60.3},
    {"name": "Owen", "age": 35, "course": "Mechanical Engineering", "marks": 49.6}, {"name": "Thabo", "age": 27, "course": "Agriculture", "marks": 66.8},
    {"name": "John", "age": 31, "course": "Nursing", "marks": 71.0}, {"name": "Willow", "age": 29, "course": "Law", "marks": 76.5}
]

#Function to add the student on the student database

def add_student(student):

    new_student = student_database.append(student)
    # print(student_database)
    return new_student


# add_student({"name": "Kay", "age": 22, "course":"Culinary", "marks": 62.4})


#Function to search for the student
def search_student():
    database = student_database
    #user input to enter the student being searched for
    name = input("Student you are searching for: ")

    for student in database:
        if name == student["name"]:
            return student        #have to get the name/ student info to be printed

    return "Student not found!"

# outcome = search_student()
# print(outcome)


#View all the students in the database
def view_students():
    database = student_database
    for student in database:
        print(f"Name: {student['name']}, Age: {student.get('age')}, Course: {student.get('course')}, Marks: {student.get('marks')}")

# view_students()



# to update the students info if needed.
def update_database():
    #go through the database
    database = student_database

    name = input("Enter students name to change their info: ")
    for student in database:
        if name == student["name"]:
            question = input("Choose what info you want to update of the student (marks/course, etc): ")
            if question == "marks":
                marks = float(input("Enter the marks of the student that you want to update: "))
                updation = student.update({"marks": marks})
                return student
            elif question == "course":
                course = input("Enter the updated course: ")
                updated_course = student.update({"course": course})
                return student
            else:
                print(f"The student info is still the same: {student['name']}, {student['age']}, {student['course']}, {student['marks']} ")
        # else:
        #     print("Name not found in database!")
    return "Name not found!"

outcome = update_database()
print(outcome)


# to delete the student from the database
def delete_student():


    #search for the name of the student
    #delete the student or what ever info
    #return the database without the deleted info
    pass








