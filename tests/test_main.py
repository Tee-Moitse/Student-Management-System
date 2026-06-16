#creating tests for the functions
#unit testing for the functions using setup for the database
#and that the different test cases dont affect database in each function test.


import main
import unittest

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
        pass
    
    def test_view_students(self):
        pass
    
    def test_update_database(self):
        pass
    
    def test_delete_student(self):
        pass
    
    
if __name__ == "__main__":
    unittest.main()
    
