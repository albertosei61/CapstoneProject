import unittest
from unittest.mock import patch, call
import tkinter as tk
import os
import re

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



def ContactInfo():
    global customer_name, customer_email, customer_address, customer_phone
    print("Enter name: ")
    customer_name = input()
    

  
    while True:
        customer_phone = input("Please enter your phone number: ")
        customer_email = input("Please enter your email address: ")
        
        # Validate phone number format
        if not re.match(r'^\d{3}-\d{3}-\d{4}$', customer_phone):
            print("Invalid phone number format. Please enter in the format XXX-XXX-XXXX.")
            continue
        
        # Validate email address format
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', customer_email):
            print("Invalid email address format. Please enter a valid email address.")
            continue
        
        # If both formats are valid, break out of the loop
        break





    print("What is your home address?")
    customer_address = input()
    print("Thank you for entering your information, it seems there was a match!. We'll be in contact with you.")
    file = open('contacts.txt', 'a')

    file.write(customer_name)
    file.write(" , ")
    file.write(customer_phone)
    file.write("\n")
    file.write(customer_email)
    file.write(",")
    file.write(customer_address)
    file.write("\n")

    file.close()

class MyApplicationTest(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_userInput(self, mock_print, mock_input):
        mock_input.side_effect = ['2021', 'Toyota', 'Corolla', 'Sedan', 'Blue', 'Leather seats']
        root = tk.Tk()
        app = MyApplication(root)
        app.userInput()

        mock_print.assert_has_calls([
            call("Enter car year: "),
            call("Enter car make: "),
            call("Enter car model: "),
            call("Enter body style preference"),
            call("Enter color preference: "),
            call("Enter car features: ")
        ], any_order=False)
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


class ContactInfoTest(unittest.TestCase):
    @patch('builtins.input')
    

    def test_ContactInfo_valid_input(self, mock_input):
        global customer_name, customer_email, customer_address, customer_phone 
        mock_input.side_effect = ['John Doe', '123-456-7890', 'johndoe@example.com', '123 Main St']
        with patch('builtins.print') as mock_print, open('contacts.txt', 'w') as mock_file:
            ContactInfo()

            mock_print.assert_called_with("Thank you for entering your information, it seems there was a match!. We'll be in contact with you.")
            mock_file_contents = mock_file.read()
            self.assertIn('John Doe , 123-456-7890', mock_file_contents)
            self.assertIn('johndoe@example.com,123 Main St', mock_file_contents)

    @patch('builtins.input')
    def test_ContactInfo_invalid_phone_number(self, mock_input):
        mock_input.side_effect = ['John Doe', '123456', 'johndoe@example.com', '123 Main St']
        with patch('builtins.print') as mock_print:
            ContactInfo()

            mock_print.assert_called_with("Invalid phone number format. Please enter in the format XXX-XXX-XXXX.")

    @patch('builtins.input')
    def test_ContactInfo_invalid_email_address(self, mock_input):
        mock_input.side_effect = ['John Doe', '123-456-7890', 'johndoe@example', '123 Main St']
        with patch('builtins.print') as mock_print:
            ContactInfo()

            mock_print.assert_called_with("Invalid email address format. Please enter a valid email address.")

if __name__ == '__main__':
    unittest.main()
    print("Tests Successfully Passed")





























# import unittest
# from unittest.mock import patch, call
# import tkinter as tk
# import os

# class MyApplication:
#     def __init__(self, root):
#         self.root = root
#         self.button = tk.Button(self.root, text="Click Here", command=self.userInput)
#         self.button.grid(column=1, row=2)

#     def userInput(self):
#         global year, make, model, body_styles, color_preference, car_features
#         print("Enter car year: ")
#         year = input()
#         inputYear(year)
#         print("Enter car make: ")
#         make = input()
#         print("Enter car model: ")
#         model = input()
#         print("Enter body style preference")
#         input1 = input()
#         body_styles = f'["{input1}"]'
#         print("Enter color preference: ")
#         color_preference = input()

#         print("Enter car features: ")
#         car_features = input()

# def inputYear(year):
#     global yearCsv
#     csv_folder_path = "../Capstone Project/us-car-models-data"
#     csv_files = [f for f in os.listdir(csv_folder_path)]
#     for filename in csv_files:
#         if year in filename:
#             yearCsv = "us-car-models-data/" + filename
#             print(yearCsv)

# class MyApplicationTest(unittest.TestCase):
#     @patch('builtins.input')
#     @patch('builtins.print')
#     def test_userInput(self, mock_print, mock_input):
#         mock_input.side_effect = ['2021', 'Toyota', 'Corolla', 'Sedan', 'Blue', 'Leather seats']
#         root = tk.Tk()
#         app = MyApplication(root)
#         app.userInput()

#         mock_print.assert_has_calls([
#             call("Enter car year: "),
#             call("Enter car make: "),
#             call("Enter car model: "),
#             call("Enter body style preference"),
#             call("Enter color preference: "),
#             call("Enter car features: ")
#         ])
#         self.assertEqual(app.button['text'], "Click Here")
#         self.assertEqual(year, '2021')
#         self.assertEqual(make, 'Toyota')
#         self.assertEqual(model, 'Corolla')
#         self.assertEqual(body_styles, '["Sedan"]')
#         self.assertEqual(color_preference, 'Blue')
#         self.assertEqual(car_features, 'Leather seats')

#     def test_inputYear(self):
#         year = '2021'
#         expected_yearCsv = 'us-car-models-data/2021.csv'
#         with patch('builtins.print') as mock_print:
#             inputYear(year)
#             mock_print.assert_called_once_with(expected_yearCsv)
#             self.assertEqual(yearCsv, expected_yearCsv)

# if __name__ == '__main__':
#     unittest.main()
#     print("Tests Successfully Passed")

































































# import unittest
# from unittest.mock import patch, mock_open
# from io import StringIO
# import tkinter as tk
# import os
# import re

# import project

# # class MyApplication:
# #     def __init__(self, root):
# #         self.root = root
# #         self.button = tk.Button(self.root, text="Click Here", command=self.userInput)
# #         self.button.grid(column=1, row=2)

    

# #     def inputYear(year):
# #         global yearCsv
# #         csv_folder_path = "../Capstone Project/us-car-models-data"
# #         csv_files = [f for f in os.listdir(csv_folder_path)]
# #         for filename in csv_files:
# #             # Passed a string to year due to conditions set for the input function
# #             if year in filename:
# #                 yearCsv = "us-car-models-data/" + filename
# #                 # print(yearCsv)
    
# #     def ContactInfo():
# #         global customer_name, customer_email, customer_address, customer_phone
# #         print("Enter name: ")
# #         customer_name = input()

# #         while True:
# #             customer_phone = input("Please enter your phone number: ")
# #             customer_email = input("Please enter your email address: ")

# #             # Validate phone number format
# #             if not re.match(r'^\d{3}-\d{3}-\d{4}$', customer_phone):
# #                 print("Invalid phone number format. Please enter in the format XXX-XXX-XXXX.")
# #                 continue

# #             # Validate email address format
# #             if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', customer_email):
# #                 print("Invalid email address format. Please enter a valid email address.")
# #                 continue

# #             # If both formats are valid, break out of the loop
# #             break

# #         print("What is your home address?")
# #         customer_address = input()
# #         print("Thank you for entering your information, it seems there was a match!. We'll be in contact with you.")
# #         file = open('contacts.txt', 'a')

# #         file.write(customer_name)
# #         file.write(" , ")
# #         file.write(customer_phone)
# #         file.write("\n")
# #         file.write(customer_email)
# #         file.write(",")
# #         file.write(customer_address)
# #         file.write("\n")

# #         file.close()



# # def userInput():
# #     global year, make, model, body_styles, color_preference, car_features

# #     print("Enter car year: ")
# #     year = input()

# #     print("Enter car make: ")
# #     make = input()
# #     print("Enter car model: ")
# #     model = input()
# #     print("Enter body style preference")
# #     input1 = input()
# #     body_styles = f'["{input1}"]'
# #     print("Enter color preference: ")
# #     color_preference = input()

# #     print("Enter car features: ")
# #     car_features = input()



# class InputYearTest(unittest.TestCase):
#     @patch('os.listdir')
#     def test_inputYear(self, mock_listdir):
#         mock_listdir.return_value = ['2021.csv', '2022.csv', '2023.csv']

#         year = '2022'
#         expected_yearCsv = 'us-car-models-data/2022.csv'

#         project.inputYear(year)
#         self.assertEqual(yearCsv, expected_yearCsv)

#     @patch('os.listdir')
#     def test_inputYear_no_match(self, mock_listdir):
#         mock_listdir.return_value = ['2021.csv', '2022.csv', '2023.csv']

#         year = '2024'
#         expected_yearCsv = None

#         project.inputYear(year)
#         self.assertEqual(yearCsv, expected_yearCsv)






# class MyApplicationTest(unittest.TestCase):
#     @patch('builtins.input')
#     @patch('builtins.print')
#     def test_userInput(self, mock_print, mock_input):
#         mock_input.side_effect = ['2021', 'Toyota', 'Corolla', 'Sedan', 'Blue', 'Leather seats']
#         root = tk.Tk()
#         app = MyApplication(root)
#         app.userInput()

#         mock_print.assert_has_calls([
#             unittest.mock.call("Enter car year: "),
#             unittest.mock.call("Enter car make: "),
#             unittest.mock.call("Enter car model: "),
#             unittest.mock.call("Enter body style preference"),
#             unittest.mock.call("Enter color preference: "),
#             unittest.mock.call("Enter car features: ")
#         ])
#         self.assertEqual(app.button['text'], "Click Here")
#         self.assertEqual(year, '2021')
#         self.assertEqual(make, 'Toyota')
#         self.assertEqual(model, 'Corolla')
#         self.assertEqual(body_styles, '["Sedan"]')
#         self.assertEqual(color_preference, 'Blue')
#         self.assertEqual(car_features, 'Leather seats')

#     def test_inputYear(self):
#         year = '2021'
#         expected_yearCsv = 'us-car-models-data/2021.csv'
#         with patch('builtins.print') as mock_print:
#             project.inputYear(year)
#             mock_print.assert_called_once_with(expected_yearCsv)
#             self.assertEqual(yearCsv, expected_yearCsv)



# class ContactInfoTest(unittest.TestCase):
#     @patch('builtins.input')
#     @patch('builtins.print')
#     @patch('builtins.open', mock_open())
#     def test_ContactInfo(self, mock_print, mock_input):
#         mock_input.side_effect = ['John Doe', '123-456-7890', 'john.doe@example.com', '123 Main St']

#         with patch('sys.stdout', new=StringIO()) as mock_stdout:
#             project.ContactInfo()

#             mock_print.assert_has_calls([
#                 unittest.mock.call("Enter name: "),
#                 unittest.mock.call("Please enter your phone number: "),
#                 unittest.mock.call("Please enter your email address: "),
#                 unittest.mock.call("What is your home address?"),
#                 unittest.mock.call("Thank you for entering your information, it seems there was a match!. We'll be in contact with you.")
#             ])

#             self.assertEqual(mock_stdout.getvalue(), "Invalid phone number format. Please enter in the format XXX-XXX-XXXX.\n")



# class UserInputTest(unittest.TestCase):
#     @patch('builtins.input')
#     @patch('builtins.print')
#     def test_userInput(self, mock_print, mock_input):
#         mock_input.side_effect = ['2021', 'Toyota', 'Corolla', 'Sedan', 'Blue', 'Leather seats']

#         userInput()

#         mock_print.assert_has_calls([
#             unittest.mock.call("Enter car year: "),
#             unittest.mock.call("Enter car make: "),
#             unittest.mock.call("Enter car model: "),
#             unittest.mock.call("Enter body style preference"),
#             unittest.mock.call("Enter color preference: "),
#             unittest.mock.call("Enter car features: ")
#         ])

#         self.assertEqual(year, '2021')
#         self.assertEqual(make, 'Toyota')
#         self.assertEqual(model, 'Corolla')
#         self.assertEqual(body_styles, '["Sedan"]')
#         self.assertEqual(color_preference, 'Blue')
#         self.assertEqual(car_features, 'Leather seats')


# if __name__ == '__main__':
#     unittest.main()
#     print("Tests Successfully Passed")
