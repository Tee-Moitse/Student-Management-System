import unittest
from main import *


class TestStudentSystem(unittest.TestCase):
    
    
    def setUp(self):
        self.database = [
            {"name": "Lisa", "age": 26, "course": "Law", "marks": 76.5},
            {"name": "Tom", "age": 24, "course": "Culinary", "marks": 65.5},
            {"name": "Sam", "age": 19, "course": "Civil Engineering", "marks": 83.8}
        ]
    
    def test_add_student(self):
        new_student = {"name": "Kay", "age": 22, "course": "Culinary", "marks": 62.4}
        add_student(self.database, new_student)
        self.assertIn(new_student, self.database)
        
    
    def test_search_student(self):
        outcome = search_student(self.database, "Lisa")
        self.assertEqual(outcome["name"], "Lisa")
    
    def test_search_student_not_found(self):
        outcome = search_student(self.database, "Lisa")
        self.assertEqual(outcome["name"], "Lisa")
    
    
    def test_view_students(self):
        view_data = view_students(self.database)
        lines = view_data.split("\n")
        self.assertEqual(len(lines), len(self.database))
        for student, line in zip(self.database, lines):
            expected_line = (
                f"Name: {student['name']}, Age: {student['age']}, "
                f"Course: {student['course']}, Marks: {student['marks']}"
            )
            self.assertEqual(line, expected_line)
        
    
    def test_update_student_info(self):
        new_info = {"name": "Tom", "age": 24, "course": "Agriculture", "marks": 70.1}
        student_update = update_student_info(self.database, new_info)
        self.assertEqual(student_update, new_info)
        
    
    def test_delete_student(self):
        student = {"name": "Lisa", "age": 26, "course": "Law", "marks": 76.5}
        student_update = delete_student(self.database, student)
        self.assertEqual(student_update, student)
        
    
    
if __name__ == "__main__":
    unittest.main()
    
