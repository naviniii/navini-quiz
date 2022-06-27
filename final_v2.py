#This is the first version of my Final code
#It combines all the components together and switches the frames

#importing tkinter and messagebox
from tkinter import *

from tkinter import messagebox as mb #importing messagebox for the end of quiz score


#configuring the window (root)
root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("800x500")
root.resizable(0,0)
root.title("General Knowledge Quiz")

#the different frames
user_details = Frame(root)
instructions = Frame(root)
quiz = Frame(root)
play_again = Frame(root)

#making the function for switching frames
for frame in (user_details, instructions, quiz, play_again):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(user_details)



#==================== User details =====================

#configuring the background colour of the user_details frame
user_details.configure(bg = "#A6F3CD")
class UserDetails:
    def __init__(self):

#the welcome label used at the top (header):
        self.welcome = Label(user_details, text = "Welcome to General Knowledge Quiz!", bg = "#A6F3CD", font=("Garamond", "30", "bold")) 
        self.welcome.place(x=175, y=20)

#the label to display to the user, to enter their name: 
        self.name = Label(user_details, text= "Please Enter your name: ", bg="#A6F3CD", font=("Garamond", "20", "bold"))
        self.name.place(x=200, y=100)

        
#The entry box for the user to enter their name: 
        self.ent_name = Entry(user_details)
        self.ent_name.place(x=400,y=100)


#The label to display to the user ,to enter their age: 
        self.age = Label(user_details, text="Please Enter your age: ", bg= "#A6F3CD", font=("Garamond", "20", "bold"))
        self.age.place(x=200, y=175)

#The entry box for the user to enter their age:
        self.ent_age = Entry(user_details)
        self.ent_age.place(x=400,y=175)

#The labels used as a warning, if the user inputs an incorrect value:
        self.warning_name = Label(user_details, text="", bg = "#A6F3CD", font=("Garamond", "20"))
        self.warning_name.place(x=400, y=135)

        self.warning_age = Label(user_details, text="", bg = "#A6F3CD", font=("Garamond", "20"))
        self.warning_age.place(x=400, y=205)

#the buttons used (next and quit). 
        self.buttons()


    def buttons(self):

#The enter button, for user to input details and move towards next portion of program: 
        btn_enter = Button(user_details, text = "Enter Details", command= self.Check_Entry, highlightbackground = "#A6F3CD", font=("Garamond", "20"))
        btn_enter.place(x=250,y=275)

#The quit button, for user to leave program:
        btn_exit = Button(user_details, text = "Quit", command=root.destroy, highlightbackground = "#A6F3CD", font=("Garamond", "20")) #root.destroy quits the program
        btn_exit.place(x=450,y=275)


#This function checks for the validity of the user's input in the NAME section: 
    def check_name(self):
        self.warning_name.config(text="")

        while len(self.ent_name.get()) >= 1:
            if all(name.isalpha() or name.isspace() for name in self.ent_name.get()):
                self.warning_name.config(text="")

                return True
            
                break
            
            
#isalpha and isspace will check to make sure no numerical or other values have been inputted.
#Checking the length of the entry is important, and having this here will make sure that there has been a value inputted. 


            else:
                self.warning_name.config(text="Invalid Name. Please enter using only letters", fg='red')
                self.ent_name.delete(0,END)
                
                return False
                break
            
        else:
            len(self.ent_name.get()) < 1
            self.warning_name.config(text="Please enter your name", fg='blue')
            return False
               
        

    
            #if the name is invalid, the entrybox will go blank again. 

#This function checks for the validity of the user's input in the AGE section:      
    def check_age(self):
        self.warning_age.config(text="")

        try:
            while len(self.ent_age.get()) >= 1:
                if int(self.ent_age.get()) >= 12 and int(self.ent_age.get())<= 18:
                    self.warning_age.config(text="")
                    return True 
#Will make sure any user using the quiz is for the designated age of 12 - 18
                
                else:
                    self.warning_age.config(text="Sorry! You must be aged 12-18 years old!", fg="red")
                    self.ent_age.delete(0,END)
                    return False

            else:
                len(self.ent_age.get()) < 1
                self.warning_age.config(text="Please enter your age", fg='blue')
                return False
#If the age inputted by the user is not between 12 - 18, the error message will show up, and the entry box will go blank

        except ValueError:
            self.warning_age.config(text="Invalid Age. Please enter numerical value.", fg="red", )
            self.ent_age.delete(0,END)
            return False
#IF the age inputted is not a numerical value, the error message will show up and the entry box will go blank.


    def Check_Entry(self):

        validate_name = self.check_name()
        validate_age = self.check_age()

        if validate_name == True and validate_age == True:
           show_frame(instructions)
           self.ent_name.delete(0, END)
           self.ent_age.delete(0,END)

        

#Calling the checking functions, and placing them under one single function, to be called in the "Enter" button. 
        
userdetails = UserDetails()


#============ Instructions ==============#

instructions.config(bg = "#A6EDF3")

instruct_file = open("instructions.txt", "r")
instruct = instruct_file.read()
instruct_file.close()

font_1 = ("Garamond","18","bold")

class Instructions:
    def __init__ (self):

        self.title = Label(instructions, text="Instructions for General Knowledge Quiz!", font=("Garamond","24","bold"), bg="#A6EDF3")
        self.title.place(x=200, y=15)

        self.instruct = Label(instructions, text = instruct, bg = "#A6EDF3", font= font_1)
        self.instruct.place(x=170,y=100)


        self.play = Button(instructions, text="Play Quiz!", command = lambda: show_frame(quiz), highlightbackground = "#A6EDF3", font = font_1)
        self.play.place(x=275, y=350)

        self.back = Button(instructions, text="Go back!", command=lambda: show_frame(user_details), highlightbackground = "#A6EDF3", font = font_1)
        self.back.place(x=400,y=350)

        

instructs = Instructions()




#================ QUIZ ===============

quiz.config(bg = "#C6A9FB")
#questions of my program. These are stored in a list variable: "q"

#importing the questions from a file, to make them modifiable by outside users. 
q=["Question 1: \nWho was the ancient greek goddess of wisdom? ",
   "Question 2: \nWhich planet has the most moons? ",
   "Question 3: \nWhich country would you find Mt Everest? ",
   "Question 4: \nWhat is the most consumed food in the world? ",
   "Question 5: \nWhere is the Eiffel Tower Located? ",
   "Question 6: \nA group of penguins is known as a: " , 
   "Question 7: \nHow many rings make up the Olympics symbol?", 
   "Question 8: \nWhat is the largest continent on Earth?: ", 
   "Question 9: \nWhich show was the most streamed on Netflix in 2021? ", 
   "Question 10: \nWho is the only egg-laying mammal?", 

   ]


#the multi-choice options of my program. These are stored in the list called: "options"
options=[
    ['Aphrodite', 'Athena', 'Persephone','Hera'],
    ['Jupiter', 'Neptune', 'Saturn','Venus'],
    ['China', 'Australia', 'Italy','Nepal'],
    ['Rice', 'Potato', 'Chicken','Lettuce'],
    ['Egypt', 'Britain', 'France','Tokyo'],
    ['Murder','Waddle','Herd','Tower'],
    ['3','4','5','6'],
    ['Antarctica','Asia','North America','Oceania'],
    ['Bridgerton','All of Us are Dead','Stranger Things','Squid Games'],
    ['Platypus','Okapi','Pangolin','Colugo'],
    ]


#the answers to the questions. These are stored in the list called: "a"

a = [2,3,4,1,3,2,3,2,4,1]

#calling the functions
class Quiz:

    def __init__(self):


        self.qn = 0

        self.ques = self.question(self.qn)


#IntVar() holds an integer value
        self.opt_selected = IntVar()

        self.opts = self.radiobtns()

        self.display_options(self.qn)

        self.buttons()

        self.correct = 0

        self.warning_select = Label(quiz, text="", bg = "#C6A9FB")
        self.warning_select.place(x=40,y=200)



    def question(self, qn):

        t = Label(quiz, text=" ~ General Knowledge Quiz ~", bg = "#C6A9FB", font = ("Helvetica", "20","bold"))

        t.place(x=265, y=15)

        qn = Label(quiz, text = q[qn], bg = "#C6A9FB", font = ("Helvetica", "15","italic"))

        qn.place(x=230, y=90)

        return qn


#the radio buttons on the questions.

    def radiobtns(self):

        val = 0

        b = []

        yp = 155

        while val < 4:

            btn = Radiobutton(quiz, text=" ", variable=self.opt_selected, value=val + 1, bg = "#C6A9FB")

            b.append(btn)

            btn.place(x=300, y=yp)

            val += 1

            yp += 40

        return b


    def display_options(self, qn):

        val = 0

        self.opt_selected.set(0)
    

        self.ques['text'] = q[qn]

        for op in options[qn]:

              self.opts[val]['text'] = op

              val += 1



    def buttons(self):

        backbutton = Button(quiz, text = "Previous Question", command=self.backbtn, highlightbackground = "#C6A9FB")

        backbutton.place(x=200,y=380)
        
        nextbutton = Button(quiz, text = "Next Question", command=self.nextbtn, highlightbackground = "#C6A9FB")
        
        nextbutton.place(x=375,y=380)

        quitbutton = Button(quiz, text = "Quit", command = lambda: show_frame(user_details), highlightbackground = "#C6A9FB")
        
        #root.destroy means end the program.

        
        quitbutton.place(x=650,y=380)



    def checkans(self, qn):

        if self.opt_selected.get() == a[qn]:

             return True

    def checkselected(self):
        
        if self.opt_selected.get() >= 1:
            self.warning_select.configure(text="")
            return True

        elif self.opt_selected.get() == 0:
            
            self.warning_select.configure(text="Please select an answer!", fg='red', font = ("Garamond", "18", "bold", "italic"))
            


    def nextbtn(self):

        x = self.checkselected()

        while x == True:

            if self.checkans(self.qn):

                self.correct += 1

            self.qn += 1

            if self.qn == len(q):

                self.display_result()
                break
        

            else:

                self.display_options(self.qn)      
                break
 

    def backbtn(self):

        while self.qn <= 9:
    
            self.qn -= 1

            if self.qn == len(q):
            
                self.display_result()

            else:
                self.display_options(self.qn)
                break

        

    def display_result(self):

        #if self.qn == 10:
            #self.answer = Button(quiz, text = "Show Results!", command = lambda: show_frame(play_again))
            #self.answer.place(x=350, y=200)
            


        score = int(self.correct / len(q) * 100)

        result = "Your Score: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "The number of correct answers you had: " + str(self.correct)
      
        wrong = "The number of incorrect answers you had: " + str(wc)

        mb.showinfo("Your Result", "\n".join([result, correct, wrong]))

    

quiz_bot=Quiz()



#===========Play Again ==============

#=========== End ==============
root.mainloop()

