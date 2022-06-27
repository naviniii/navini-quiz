from tkinter import *


root = Tk()
root.geometry("800x500")

class UserDetails:
    def __init__ (self):

        self.welcome = Label(root, text = "welcome to gen know quiz") #add font/colour
        self.welcome.place(x=100, y=10)

        self.name = Label(root, text= "testing the name")
        self.name.place(x=100, y=25)

        self.ent_name = Entry(root)
        self.ent_name.place(x=200,y=25)

        self.age = Label(root, text="testing the age")
        self.age.place(x=100, y=75)

        self.ent_age = Entry(root)
        self.ent_age.place(x=200,y=75)

        self.warning_name = Label(root, text="")
        self.warning_name.place(x=350, y=25)

        self.warning_age = Label(root, text="")
        self.warning_age.place(x=350, y=75)

        self.buttons()


    def buttons(self):
        btn_enter = Button(root, text = "Enter", command=self.Check_Entry)
        btn_enter.place(x=200,y=150)
        btn_exit = Button(root, text = "Quit", command=root.destroy)
        btn_exit.place(x=300,y=150)



    def check_name(self):
        self.warning_name.config(text="")

        if all(name.isalpha() or name.isspace() for name in self.ent_name.get()):
            self.warning_name.config(text="good")
        
        else:
            self.warning_name.config(text="Invalid Name. Please enter alpha values", fg='red')
            
    def check_age(self):
        self.warning_age.config(text="")

        try:
            int(self.ent_age.get())
            self.warning_age.config(text="good")

        except ValueError:
            self.warning_age.config(text="Invalid Age. Please enter numerical value.", fg="red")

    def Check_Entry(self):
        self.check_name()
        self.check_age()
        
user_details = UserDetails()    
root.mainloop()
