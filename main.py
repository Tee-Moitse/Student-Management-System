from database import student_database


def add_student(student):

    new_student = student_database.append(student)
    # print(student_database)
    return new_student


# add_student({"name": "Kay", "age": 22, "course":"Culinary", "marks": 62.4})


#Function to search for the student
def search_student():

    database = student_database
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
        return f"Name: {student['name']}, Age: {student.get('age')}, Course: {student.get('course')}, Marks: {student.get('marks')}"

view_students()



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

    return "Student not found!⚠️"



# result = delete_student()
# print(result)












