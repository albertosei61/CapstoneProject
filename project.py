import tkinter as tk
import PyPDF2 
from PIL import Image, ImageTk
import os

import csv, glob
from fpdf import FPDF
from reportlab.pdfgen.canvas import Canvas
from datetime import datetime
import re


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)
root.title("ALL MOTOR UNIVERSE")

#Image position and resize for graphical user interface
baseWidth = 400
logo = Image.open('car-logo.jpg')
wpercent = (baseWidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((baseWidth,hsize), Image.Resampling.LANCZOS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#User prompt on main page
guide = tk.Label(root, text="", font="Raleway")
guide.grid(columnspan=3, column=0, row=1)


#User input and then append match to print()  
#Function to get user input. Also another button will be created to exit function
#Parameters are Car Brand, or model, year, mileage, type(sedan etc.)
def inputYear(year):
    global yearCsv
    csv_folder_path = "../Capstone Project/us-car-models-data"
    csv_files = [f for f in os.listdir(csv_folder_path)]
    for filename in csv_files:
        #Passed a string to year due to conditions set for input function
        if year in filename:
            yearCsv = "us-car-models-data/" + filename
            #print(yearCsv)



def csvSet():
    try:
        # initializing the titles and rows list
        fields = []
        rows = [year, make, model, body_styles]
        
        inputYear(year)
        # reading csv file
        filename = yearCsv
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                if make.lower() == row[1].lower() and model.lower() == row[2].lower() and body_styles.lower() == row[3].lower():
                    csv_make = row[1]
                    csv_model = row[2]
                    csv_body_styles = row[3]  

                    formatted_string = "Year: {}\nMake: {}\nModel: {}\nBody styles: {}".format(year, csv_make, csv_model, csv_body_styles[2:-2])

                    print(formatted_string)

                    #New PDF page

                    pdf = Canvas("car_interest.pdf")         

                    pdf.setTitle("Dealership Car Interest Paper")       

                    pdf.setFont("Helvetica-Bold", 16)

                    pdf.drawCentredString(300, 750, "Dealership Car Interest Paper")

                    pdf.setFont("Helvetica", 12)

                    now = datetime.now()
                    date_time = now.strftime("%m/%d/%Y %H:%M:%S")

                    pdf.drawString(50, 700, f"Date and Time: {date_time}")

                    pdf.drawString(50, 650, f"Name: {customer_name}")

                    pdf.drawString(50, 600, f"Email: {customer_email}")

                    pdf.drawString(50, 550, f"Phone Number: {customer_phone}")

                    pdf.drawString(50, 500, f"Address: {customer_address}")

                    pdf.drawString(50, 450, f"Car Make and Model of Interest: {csv_make} {csv_model}")

                    pdf.drawString(50, 400, f"Color of Car of Interest: {color_preference}")

                    pdf.drawString(50, 350, f"Features of Car of Interest: {car_features}")

                    pdf.setFont("Helvetica", 8)
                    # write a dealer special message.
                    pdf.drawString(50, 300, "Disclaimer: This document does not guarantee the availability or price of the car of interest.")

                    pdf.save()
                    #print("See pdf page for more information")
    
    except FileNotFoundError:
        print("File not found!")
    except IndexError:
        print("Invalid CSV format: Index out of range!")
    except Exception as e:
        print("An error occurred:", str(e))
    




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



def userInput():
    global year, make, model, body_styles, color_preference, car_features
    
        #current_year = datetime.now().year +1
    # current_year = 2024
    # year = input("Enter Year Here! Type quit to stop >>")
    # if year == "":
    #     year = current_year
        #else:
        #    year = int(year)

    #year = int(year) if year else current_year
    # while True:
    #     if not 1992 < year < current_year:
    #         print("Please specify a date between 1992 to {}".format(current_year))
        
    #     else:
    #         print('We have inventory for that year')

    print("Enter car year: ")
    year = input()


    print("Enter car make: ")
    make = input()
    print("Enter car model: ")
    model= input()
    print("Enter body style preference")
    input1 = input()
    body_styles = f'["{input1}"]'
    print("Enter color preference: ")
    color_preference = input()

    print("Enter car features: ")
    car_features = input()

userInput()




ContactInfo()
csvSet()



        

                    

def printPDF():
 #   results = 'formatted_string'
  #  pdf = FPDF()
   # pdf.add_page()
    #pdf.set_font("Arial","B",16)
    #pdf.write(4,"Hello thank you for taking the time to search our inventory!")
    #pdf.cell(200,10, txt=results, ln=1, align="C")
    #pdf.output("file.pdf")

    print("Here") 








#Button on main page// Will take us to user inputs.
button_text = tk.StringVar()
button_btn = tk.Button(root, textvariable=button_text, command=lambda:userInput(), font="Raleway", bg="slategray", fg="white", height=2, width=15)
button_text.set("Click Here")
button_btn.grid(column=1, row=2)


root.mainloop()

