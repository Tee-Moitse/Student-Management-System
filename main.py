from database import student_database


def add_student(database, student):

    new_student = database.append(student)
    return new_student


# add_student({"name": "Kay", "age": 22, "course":"Culinary", "marks": 62.4})


#Function to search for the student
def search_student(database, name):

    for student in database:
        if name == student["name"]:
            return student        #have to get the name/ student info to be printed

    return None

# outcome = search_student()
# print(outcome)


#View all the students in the database
def view_students(database):
    lines = []

    for student in database:
        lines.append(
            f"Name: {student['name']}, Age: {student.get('age')}, "
            f"Course: {student.get('course')}, Marks: {student.get('marks')}"
        )
        
    return "\n".join(lines)



# to update the students info if needed.
def update_student_info(database, name, update):

    for student in database:
        if student["name"] == name:
            student.update(update)
    return None

# outcome = update_database()
# print(outcome)


# to delete the student from the database
def delete_student():

    database = student_database

    name = input("Enter the student's name of whom you want to delete: ")

    first_length = len(database)

    student_d = [student for student in database if student.get('name') != name]


    if len(student_d) < first_length:
        return f"Successfully deleted {name}!"

    return "Student not found!"



# result = delete_student()
# print(result)












