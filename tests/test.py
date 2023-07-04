import unittest
import sys
import os

# Adding parent directory to path to import the script with the process_answer_sheet function
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import process_answer_sheet  

class TestAnswerSheetAnalysis(unittest.TestCase):

    def setUp(self):
        self.template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "example.json")

    def test_image1(self):
        expected_result = {
            "questions": [["A"], ["D"], ["B"], ["C"], ["D"], ["A"], ["C"], ["B"], ["D"], ["B"], ["C"], ["C"], ["D"], ["B"], ["A"], ["D"],["B"], ["C"], ["A"], ["A"]],
            "student_info": [["1"], ["6"], ["8"], ["2"]]
        }
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test1.png")
        result = process_answer_sheet(image_path, self.template_path)
        self.assertEqual(result, expected_result)

    def test_image2(self):
        expected_result = {
            "questions": [["A"], ["B", "D"], ["D"], ["A", "C"], ["B", "D"], ["C"], ["D"], ["B"], ["A", "D"], ["A", "C", "D"], ["A"], ["B", "D"], ["C"], ["A", "B", "C", "D"], ["C"], ["A"], ["B", "D"], ["D"], ["B"], ["A", "D"]],
            "student_info": [["1", "3", "5"], ["2", "6", "8"], ["5", "7", "8", "9"], ["2", "4", "0"]]
        }
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test2.png")
        # Call the analyze_answer_sheet function
        result = process_answer_sheet(image_path, self.template_path)
        # Compare results
        self.assertEqual(result, expected_result)

    def test_image3(self):
        # Define expected result for test3.png
        expected_result = {
            "questions": [["D"], ["B"], [], ["D"], ["A"], ["C"], ["B"], ["C"], ["D"], ["A"], ["D"], ["A"], ["C"], ["B"], ["A"], ["B"], ["A"], ["B"], [], ["B"]],
            "student_info": [["6"], ["5"], ["3"], ["9"]]
        }
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test3.jpg")
        # Call the analyze_answer_sheet function
        result = process_answer_sheet(image_path, self.template_path)
        # Compare results
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()