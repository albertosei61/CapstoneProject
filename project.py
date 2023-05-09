import tkinter as tk
import PyPDF2 
from PIL import Image, ImageTk
import os

import csv, glob
from fpdf import FPDF
from reportlab.pdfgen.canvas import Canvas
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
guide = tk.Label(root, text="Click to get in your dream car TODAY", font="Raleway")
guide.grid(columnspan=3, column=0, row=1)


#User input and then append match to print()  
#Function to get user input. Also another button will be created to exit function
#Parameters are Car Brand, or model, year, mileage, type(sedan etc.)


def inputYear(year):
        global yearCsv
        csv_folder_path = "../Capstone Project/us-car-models-data"
        csv_files = [f for f in os.listdir(csv_folder_path)]
        for filename in csv_files:
            if year in filename:
                yearCsv = "us-car-models-data/" + filename
                print(yearCsv)

    
def userInput():
    global year, make, model, body_styles
    print("Enter car year: ")
    year = input()
    inputYear(year)
    print("Enter car make: ")
    make = input()
    print("Enter car model: ")
    model= input()
    print("Enter body style preference")
    input1 = input()
    body_styles = f'["{input1}"]'
    #phone = input("Enter phone number")

    #with open('us-car-models-data/2020.csv', 'r') as file:
        #csvFile = csv.reader(file)
        #for line in csvFile:
            #print(line)
            #contactInfo()
    ContactInfo()





        

#def contactInfo():
    #name = input("Enter your name")
    #phone = input("Enter your phone number:")

    #phone_number()
def csvSet():
    try:
        # initializing the titles and rows list
        fields = []
        rows = [year, make, model, body_styles]

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

                    pdf_filename = "file.pdf"
                    pdf = Canvas(pdf_filename)

                    # Set up the canvas and positioning for text
                    pdf.setFont("Helvetica", 12)
                    x = 100
                    y = 700
                    greeting = "Hello thank you for taking the time to search our inventory!. We will contact you within 24 hours after request if it falls on a business day.\
                            Thank you"
                    pdf.drawString(20, 800, greeting)
        

                    # Write the formatted string to the PDF
                    pdf.drawString(x, y, formatted_string)

                    # Save the PDF
                    pdf.save()

                    printPDF()
    
    except FileNotFoundError:
        print("File not found!")
    except IndexError:
        print("Invalid CSV format: Index out of range!")
    except Exception as e:
        print("An error occurred:", str(e))
                    

def printPDF():
 #   results = 'formatted_string'
  #  pdf = FPDF()
   # pdf.add_page()
    #pdf.set_font("Arial","B",16)
    #pdf.write(4,"Hello thank you for taking the time to search our inventory!")
    #pdf.cell(200,10, txt=results, ln=1, align="C")
    #pdf.output("file.pdf")

    print("Here") 
    
       
                    
                
                    
#except Exception as e:
     #print("An error occured: {}".format(e))


                    
 
        # get total number of rows
        #print("Total no. of rows: %d"%(csvreader.line_num))
 
    # printing the field names
   # print('Field names are:' + ', '.join(field for field in fields))
 
    # printing first 5 rows
   # print('\nFirst 5 rows  are:\n')
   # for row in rows[:5]:
        # parsing each column of a row
       # for col in row:
            #print("%10s"%col,end=" "),
        #print('\n')
    


        #results()

    
    




#def results():
     



def ContactInfo():
    print("Enter name: ")
    firstInput = input()

    print("What is your phone number: ")
    secInput = input()

    file = open('contacts.txt', 'a')

    file.write(firstInput)
    file.write(" , ")
    file.write(secInput)
    file.write("\n")

    file.close()


    csvSet()


    





    
  



#Button on main page// Will take us to user inputs.
button_text = tk.StringVar()
button_btn = tk.Button(root, textvariable=button_text, command=lambda:userInput(), font="Raleway", bg="slategray", fg="white", height=2, width=15)
button_text.set("Click Here")
button_btn.grid(column=1, row=2)


root.mainloop()

