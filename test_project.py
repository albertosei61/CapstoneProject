import unittest
from unittest.mock import patch
import tkinter as tk
import os

class MyApplication:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text="Click Here", command=self.userInput)
        self.button.grid(column=1, row=2)

    def userInput(self):
        global year, make, model, body_styles, color_preference, car_features
        print("Enter car year: ")
        year = input()
        inputYear(year)
        print("Enter car make: ")
        make = input()
        print("Enter car model: ")
        model = input()
        print("Enter body style preference")
        input1 = input()
        body_styles = f'["{input1}"]'
        print("Enter color preference: ")
        color_preference = input()

        print("Enter car features: ")
        car_features = input()

def inputYear(year):
    global yearCsv
    csv_folder_path = "../Capstone Project/us-car-models-data"
    csv_files = [f for f in os.listdir(csv_folder_path)]
    for filename in csv_files:
        if year in filename:
            yearCsv = "us-car-models-data/" + filename
            print(yearCsv)

class MyApplicationTest(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_userInput(self, mock_print, mock_input):
        mock_input.side_effect = ['2021', 'Toyota', 'Corolla', 'Sedan', 'Blue', 'Leather seats']
        root = tk.Tk()
        app = MyApplication(root)
        app.userInput()

        mock_print.assert_has_calls([
            unittest.mock.call("Enter car year: "),
            unittest.mock.call("Enter car make: "),
            unittest.mock.call("Enter car model: "),
            unittest.mock.call("Enter body style preference"),
            unittest.mock.call("Enter color preference: "),
            unittest.mock.call("Enter car features: ")
        ])
        self.assertEqual(app.button['text'], "Click Here")
        self.assertEqual(year, '2021')
        self.assertEqual(make, 'Toyota')
        self.assertEqual(model, 'Corolla')
        self.assertEqual(body_styles, '["Sedan"]')
        self.assertEqual(color_preference, 'Blue')
        self.assertEqual(car_features, 'Leather seats')

    def test_inputYear(self):
        year = '2021'
        expected_yearCsv = 'us-car-models-data/2021.csv'
        with patch('builtins.print') as mock_print:
            inputYear(year)
            mock_print.assert_called_once_with(expected_yearCsv)
            self.assertEqual(yearCsv, expected_yearCsv)

if __name__ == '__main__':
    unittest.main()
    print("Tests Successfully Passed")
