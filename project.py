import tkinter as tk
import PyPDF2 
from PIL import Image, ImageTk

root = tk.Tk()


canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)
root.title("ALL MOTOR UNIVERSE")


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


#Function to get user input. Also another button will be created to exit function
def userInput():
    print("Succesfully got to the first function")
    




#Button on main page// Will take us to user inputs.
button_text = tk.StringVar()
button_btn = tk.Button(root, textvariable=button_text, command=lambda:userInput(), font="Raleway", bg="slategray", fg="white", height=2, width=15)
button_text.set("Click Here")
button_btn.grid(column=1, row=2)







root.mainloop()

