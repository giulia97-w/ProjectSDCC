import tkinter as tk
import requests #Requests allows you to send HTTP/1.1 requests
from tkinter import *
from PIL import Image, ImageTk #The Python Imaging Library adds image processing capabilities to the Python interpreter
from tkinter import ttk #The tkinter.ttk module provides access to the Tk themed widget set
import json #JSON module for converting the datastructures to JSON strings
import datetime
#Tkinker is a python module used to develop GUI (Graphical User Interface) applications



#creating tkinker window
window = tk.Tk()
#creating fixed geometry of the tkinker window 
window.geometry("1300x900")
#creating the title of the window
window.title("COVID 19 VACCINE - MAIN INFORMATIONS ")
#grid lets you layout widgets in columns and rows
window.grid_columnconfigure(0, weight=20)
#configuration options
window.configure(background = 'white')
#Static window
window.resizable(width=0, height=0)


#opening the image
background_image = Image.open("covidCell.jpg")
#Add image file
background_photo = ImageTk.PhotoImage(background_image)
#show image using label
background_label = tk.Label(window, image = background_photo)
background_label.image = background_photo
background_label.place(relwidth=1, relheight=1)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def date(expire):
    
    try:
        datetime.datetime.strptime(expire, '%d/%m/%Y')
        return True
    except ValueError:
        return False
   



    #function to create a new window
#Toplevel widgets work as windows that are directly managed by the window manager.
def createNewWindow():
    newWindow = tk.Toplevel(window)
    newWindow.resizable(width=0, height=0)
    labelExample = tk.Label(newWindow, text = "COVID 19 VACCINE", font=('Helvetica bold',32))
    newWindow.geometry("1300x900")
    newWindow.grid_columnconfigure(0, weight=20)
    labelExample.grid()
    buttonOperation.grid(row = 260)
    buttonOperation.place(relx=0.81, rely=0.60)
    
    
    #opening the image
    background_image = Image.open("covidCell.jpg")
    #add image file
    background_photo = ImageTk.PhotoImage(background_image)
    #show image using label
    background_label = tk.Label(newWindow, image = background_photo)
    background_label.image = background_photo
    background_label.place(relwidth=1, relheight=1)
    
    
    #label implements a display box where you can place text or images
    newWelcome_label = tk.Label(newWindow,
                                text="COVID 19 VACCINE",
                                        font=("Helvetica bold", 32), bg='medium aquamarine', fg = 'black')
    newWelcome_label.grid(row=0, column=0, sticky="WE", padx=300, pady=10)
    
    
    #get_vax() function to get vaccine information by entering the lot
    def get_vax():
        if text_input.get():
            user_input = text_input.get()
            lotto =  user_input
            response = requests.get("https://soy1zqqas4.execute-api.us-east-1.amazonaws.com/prod1/getitem?lotto=" + lotto,
                                    params=lotto).json()
     
        else:
            response = "Enter the vaccine batch"
            
        #Text widgets provide advanced capabilities that allow you to edit a multiline text and format the way it has to be displayed, such as changing its color and font.
        textwidget = tk.Text(newWindow, height=4)
        textwidget.insert(tk.END, text_parsing(response))
        textwidget.grid(row=4, column=0, sticky="WE", padx=300, ipady = 10)
       
    #label implements a display box where you can place text or images
    ttk.Label(newWindow, text= 'Enter the batch of the vaccine you want to search for:', font=('Helvetica', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE")
    
    #The Entry widget is used to accept single-line text strings from a user
    text_input = tk.Entry(newWindow, font=('Helvetica', 10))
    text_input.grid(row=2, column=0, sticky="WE", padx=300)
    
    #SEND BUTTON
    download_button = tk.Button(newWindow, text="SEND", command=get_vax, font = ('Helvetica',12), bg = 'medium aquamarine', relief = RAISED, width=1,
                               height=1, activebackground='lightblue3', cursor = 'hand2', bd = 1)
    download_button.grid(row=7, column=0, sticky="WE", pady=10, padx=300)
    
    #delete_vax() function to delete a vaccine record by entering the batch  
    def delete_vax():
        if second_text_input.get():
            user_input = second_text_input.get()
            lotto =  user_input
            response = requests.get("https://soy1zqqas4.execute-api.us-east-1.amazonaws.com/prod1/deleteitem?lotto=" + lotto,
                                    params=lotto).json()

        else:
            response = "Enter the vaccine batch"
        
        
        textwidget = tk.Text(newWindow, height=2)
        textwidget.insert(tk.END, response)
        textwidget.grid(row=23, column=0, sticky="WE", padx=300, pady=10)
    
    #The purpose of this widget is to display text, an image, or both. Generally the content is static, but your program can change the text or the image, in this case is static
    ttk.Label(newWindow, text= 'Enter the batch of the vaccine you want to delete:', font=('Helvetica', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE")
    

    #The Entry widget is used to accept single-line text strings from a user
    #Batch input for the delete function
    second_text_input = tk.Entry(newWindow, font=('Helvetica', 10))
    second_text_input.grid(row=20, column = 0, sticky = "WE", padx  =300)
    
    #DELETE BUTTON
    second_button = tk.Button(newWindow, text="DELETE VACCINE", command=delete_vax, font = ('Helvetica',12), bg = 'medium aquamarine', relief = RAISED, width=1,
                               height=1, activebackground='lightblue3', cursor = 'hand2', bd = 1 )
    second_button.grid(row=26, column=0, pady=10, sticky="WE", padx = 300)
    
    
       
    #update_vax() function to update the information on the expiration of a vaccine in the table
    def update_vax():
        if firth_input.get():
            user_input = firth_input.get()
            third_user_input = firth_inputC.get()
            lotto =  user_input
            numeroDosiPerVaccino = third_user_input
            if is_number(numeroDosiPerVaccino):
                response = requests.get("https://soy1zqqas4.execute-api.us-east-1.amazonaws.com/prod1/updateitem?lotto=" + lotto +  "&numeroDosiPerVaccino=" + numeroDosiPerVaccino , params=lotto).json()
               
            else: 
                response =  {
                    "number of doses for vaccine must be an integer" }
                
                   
        else:
            response = "Enter the vaccine batch followed by the information that you want to change"

        textwidget = tk.Text(newWindow, height = 2)
        textwidget.insert(tk.END, response)
        textwidget.grid(row=175, column=0, sticky="WE", padx=300, pady=10)
    
    
    #The purpose of this widget is to display text, an image, or both. Generally the content is static, but your program can change the text or the image, in this case is static
    ttk.Label(newWindow, text= 'Enter the batch of the vaccine whose number of doses you want to change:', font=('Century Schoolbook bold', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE")
    
    #batch input for the update function
    firth_input = tk.Entry(newWindow, font=('Century Schoolbook bold', 10))
    firth_input.grid(row=110, column=0, sticky="WE", padx=300) 

    
    ttk.Label(newWindow, text= 'Enter the new number of doses of the vaccine:', font=('Century Schoolbook bold', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE")
    
    #number of doses for vaccine input for the update function
    firth_inputC = tk.Entry(newWindow, font=('Century Schoolbook bold', 10))
    firth_inputC.grid(row=120, column=0, sticky="WE", padx=300) 
    
    #UPDATE BUTTON   
    firth_button = tk.Button(newWindow, text="UPDATE THE DEADLINE", command=lambda : update_vax(), font = ('Helvetica',12), bg = 'medium aquamarine', relief = RAISED,width=1,
                               height=1, activebackground='lightblue3', cursor = 'hand2', bd = 1)
    firth_button.grid(row=400, column=0, sticky="WE", pady=10, padx=300)
    
    #EXIT BUTTON
    exit_button = tk.Button(newWindow, text = "EXIT", command=lambda : close(), font=('Helvetica',12), relief = RAISED, activebackground='lightblue3', cursor = 'hand2', bg = 'white', bd = 1)
    exit_button.grid( sticky='NE', row = 450, padx = 60)
    exit_button.place(relx=0.93, rely=0.01, relwidth=0.05, relheight=0.05)
    
       
            
#scan_vax() function to scan the dynamoDB "VaxTables" table
def scan_vax():

    #requests has built-in .json() method   
    response = requests.get("https://soy1zqqas4.execute-api.us-east-1.amazonaws.com/prod1/scanitem").json()
    #json.dumps: Serialize obj to a JSON formatted str using a conversion table.
    text_response = json.dumps(response, indent=6)
    
    
    textwidget = tk.Text(height = 7)
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=50, column=0, sticky="WE", padx=300, pady=10)
    
#Add buttons in the master window
#GET DATABASE INFORMATION BUTTON
third_button = tk.Button(text="GET DATABASE INFORMATION", command=scan_vax, font = ('Helvetica', 12), bg = 'medium aquamarine', relief = RAISED, width=1,
                           height=1, activebackground='lightblue3', cursor = 'hand2', bd = 1)
third_button.grid(row=41, column=0, pady=10, sticky="WE", padx = 300)    



# insert_vax() function for inserting new records into the DynamoDb table by entering information by the user    
def insert_vax():
    if fifth_input.get():
        user_input4 = fifth_input.get()
        user_input5 = fifth_inputB.get()
        user_input6 = fifth_inputC.get()
        user_input7 = fifth_inputD.get()
        user_input8 = fifth_inputE.get()
        lotto =  user_input4
        scadenza = user_input8
        casaFarmaceutica = user_input6
        nomeVaccino = user_input5
        numeroDosiPerVaccino = user_input7
        if date(scadenza) and is_number(numeroDosiPerVaccino):
            response = requests.get("https://soy1zqqas4.execute-api.us-east-1.amazonaws.com/prod1/insertvax?lotto=" + lotto + "&nomeVaccino=" + nomeVaccino + "&casaFarmaceutica=" + casaFarmaceutica + "&numeroDosiPerVaccino=" + numeroDosiPerVaccino + "&scadenza=" + scadenza, params=lotto).json()

        else:
            response = {
             "Invalid Date or number of doses for vaccine: Date must be in format dd/mm/yyyy and the number of doses must be an integer",
            }
        
    else:
        response = "Enter the information about the vaccine you want to add"

    textwidget = tk.Text(height = 3)
    textwidget.insert(tk.END, response)
    textwidget.grid(row=200, column=0, sticky="WE", padx=300, pady=10)

    

#The purpose of this widget is to display text, an image, or both. Generally the content is static, but your program can change the text or the image, in this case is static
ttk.Label(window, text= 'Enter batch:', font=('Century Schoolbook bold', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE", row = 80)


#The Entry widget is used to accept single-line text strings from a user
#batch input for the insert function
fifth_input = tk.Entry(font=('', 10))
fifth_input.grid(row=90, column=0, sticky="WE", padx=300) 


ttk.Label(window, text= 'Enter the name of the Vaccine:', font=('Century Schoolbook bold', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE", row = 91)

#name input for the insert function
fifth_inputB = tk.Entry(font=('', 10))
fifth_inputB.grid(row=92, column=0, sticky="WE", padx=300) 


ttk.Label(window, text= 'Enter pharmaceutical company:', font=('Century Schoolbook bold', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE", row = 93)

#pharmaceutical company input for the insert function
fifth_inputC = tk.Entry(font=('Century Schoolbook bold', 10))
fifth_inputC.grid(row=94, column=0, sticky="WE", padx=300) 


ttk.Label(window, text= 'Enter number of doses per vaccine', font=('Century Schoolbook bold', 10), background = 'medium aquamarine').grid(padx = 300, sticky="WE",row = 95 )


#number of doses input for the insert function
fifth_inputD = tk.Entry(font=('Century Schoolbook bold', 10))
fifth_inputD.grid(row=96, column=0, sticky="WE", padx=300) 


ttk.Label(window, text= 'Enter expiration:', font=('Century Schoolbook bold', 10), background = 'medium aquamarine' ).grid(padx = 300, sticky="WE", row = 97)


#exiparion input for the insert function
fifth_inputE = tk.Entry(font=('Century Schoolbook bold', 10))
fifth_inputE.grid(row=98, column=0, sticky="WE", padx=300) 

#ADD BUTTON
fifth_button = tk.Button(text="ADD VACCINE", command=insert_vax, font = ('Helvetica',12), bg = 'medium aquamarine', relief = RAISED, width=1,
                           height=1, activebackground='lightblue3', cursor = 'hand2', bd = 1)
fifth_button.grid(row=250, column=0, sticky="WE", pady=5, padx=300)
    


#close () function to close windows using a button on both pages   
def close():
    window.destroy()

    
def text_parsing(text_response):
    if 'lotto' in text_response:
        return  'BATCH = ' + text_response['lotto'] + '\n' + \
                'Vaccine name = ' + text_response['nomeVaccino'] + '\n' + \
                'Pharmaceutical company = ' + text_response['casaFarmaceutica'] + '\n' + \
                'Number of doses per vaccine = ' + text_response['numeroDosiPerVaccino'] + '\n' + \
                'Expiration = ' + text_response['scadenza'] + '\n'
    elif 'errorMessage' in text_response:
        return text_response['errorMessage']
    else:
        return text_response


    
    
    
#label in the master window    

welcome_label = tk.Label(window,
                            text="COVID 19 VACCINE",
                                    font=("Helvetica", 30), bg='medium aquamarine', fg = 'black')
welcome_label.grid(row=0, column=0, sticky="WE", padx=300, pady=10)




#EXIT BUTTON
exit_button = tk.Button(window, text = "EXIT", command=lambda : close(), bd=1, font=('Helvetica',12), relief = RAISED, activebackground='lightblue3', cursor = 'hand2', bg = 'white')
exit_button.grid( sticky='NE', padx= 60)
exit_button.place(relx=0.90, rely=0.01, relwidth=0.05, relheight=0.05)


#OTHER OPERATIONS BUTTON
buttonOperation = tk.Button(window, 
              text="OTHER OPERATIONS",
              command=createNewWindow, bd=1, font=('Helvetica',12), relief = RAISED, bg = 'medium aquamarine', activebackground='lightblue3', cursor = 'hand2')
buttonOperation.grid(row=260,  sticky='N')
buttonOperation.place(relx=0.81, rely=0.60)



if __name__ == "__main__":
# Execute Tkinter   
    window.mainloop()
