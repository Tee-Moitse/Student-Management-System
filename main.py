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
    {"name": "John", "age": 31, "course": "Nursing", "marks": 71.0}, {"name": "Willow", "age": 29, "course": "Law", "marks": 76.5},
]

#Function to add the student on the student database

def add_student(student):

    new_student = student_database.append(student)
    print(student_database)
    return new_student


add_student({"name": "Kay", "age": 22, "course":"Culinary", "marks": 62.4})


#Function to search for the student
def search_student(studen_database):
    pass

#Function to view the students for the database
def view_student(student_database):
    pass







