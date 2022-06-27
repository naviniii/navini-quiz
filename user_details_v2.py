#this is the second version of my user details page, which includes the changes such as:
#- changing the boundary values
#- changing the placement of the label, entry boxes and buttons.



#importing the tkinter module

from tkinter import *

#creating the window and window size
root = Tk()
root.geometry("800x500")


#creating the class to house the functions
class UserDetails:
    def __init__ (self):

#the welcome label used at the top (header):
        self.welcome = Label(root, text = "Welcome to General Knowledge Quiz") #add font/colour
        self.welcome.place(x=275, y=20)

#the label to display to the user, to enter their name: 
        self.name = Label(root, text= "Please Enter your name")
        self.name.place(x=150, y=75)

        
#The entry box for the user to enter their name: 
        self.ent_name = Entry(root)
        self.ent_name.place(x=300,y=75)


#The label to display to the user ,to enter their age: 
        self.age = Label(root, text="Please Enter your age")
        self.age.place(x=150, y=130)

#The entry box for the user to enter their age:
        self.ent_age = Entry(root)
        self.ent_age.place(x=300,y=130)

#The labels used as a warning, if the user inputs an incorrect value:
        self.warning_name = Label(root, text="")
        self.warning_name.place(x=500, y=75)

        self.warning_age = Label(root, text="")
        self.warning_age.place(x=500, y=135)

#the buttons used (next and quit). 
        self.buttons()


    def buttons(self):

#The enter button, for user to input details and move towards next portion of program: 
        btn_enter = Button(root, text = "Enter", command=self.Check_Entry)
        btn_enter.place(x=250,y=250)

#The quit button, for user to leave program:
        btn_exit = Button(root, text = "Quit", command=root.destroy) #root.destroy quits the program
        btn_exit.place(x=350,y=250)


#This function checks for the validity of the user's input in the NAME section: 
    def check_name(self):
        self.warning_name.config(text="")

        while len(self.ent_name.get()) >= 1:
            if all(name.isalpha() or name.isspace() for name in self.ent_name.get()):
                self.warning_name.config(text="Hello!")
                break
            
            
#isalpha and isspace will check to make sure no numerical or other values have been inputted.
#Checking the length of the entry is important, and having this here will make sure that there has been a value inputted. 


            else:
                self.warning_name.config(text="Invalid Name. Please enter using only letters", fg='red')
                self.ent_name.delete(0,END)
                break
            
        else:
            len(self.ent_name.get()) < 1
            self.warning_name.config(text="Please enter your name", fg='blue')
               
            
#This function checks for the validity of the user's input in the AGE section:      
    def check_age(self):
        self.warning_age.config(text="")

        try:
            if int(self.ent_age.get()) >= 12 and int(self.ent_age.get())<= 18:
                self.warning_age.config(text="good")
#Will make sure any user using the quiz is for the designated age of 12 - 18

                
            else:
                self.warning_age.config(text="Sorry! You must be aged 12-18 years old!")
                self.ent_age.delete(0,END)
#If the age inputted by the user is not between 12 - 18, the error message will show up, and the entry box will go blank

                
        except ValueError:
            self.warning_age.config(text="Invalid Age. Please enter numerical value.", fg="red")
            self.ent_age.delete(0,END)
#IF the age inputted is not a numerical value, the error message will show up and the entry box will go blank.


    def Check_Entry(self):
        self.check_name()
        self.check_age()

#Calling the checking functions, and placing them under one single function, to be called in the "Enter" button. 
        
user_details = UserDetails()    
root.mainloop()
