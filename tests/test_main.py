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
        view_data = self.database
        self.assertEqual(view_data, "Name: Lisa, Age: 26, Course: 76.5")
        pass
    
    def test_update_database(self):
        pass
    
    def test_delete_student(self):
        pass
    
    
if __name__ == "__main__":
    unittest.main()
    
