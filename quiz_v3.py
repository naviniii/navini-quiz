#this program is the quiz-component of my program


#exporting tkinter from external library
from tkinter import *
from tkinter import messagebox as mb #importing messagebox for the end of quiz score


#questions of my program. These are stored in a list variable: "q"
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
a=[2,3,4,1,3,2,3,2,4,1]



#starting the program
#to run the window called root
root = Tk()

#the size of the window
root.geometry("800x500")
root.configure(bg = "#ccecf0")

#the title of the window
root.title("General Knowledge Quiz")


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



    def question(self, qn):

        t = Label(root, text=" ~ General Knowledge Quiz ~", bg = "#ccecf0", font = ("Helvetica", "20","bold"))

        t.place(x=265, y=15)

        qn = Label(root, text = q[qn], bg = "#ccecf0", font = ("Helvetica", "15","italic"))

        qn.place(x=230, y=90)

        return qn


#the radio buttons on the questions.

    def radiobtns(self):

        val = 0

        b = []

        yp = 155

        while val < 4:

            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, bg = "#ccecf0")

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

        backbutton = Button(root, text = "Previous Question", command=self.backbtn, highlightbackground = "#ccecf0")

        backbutton.place(x=200,y=380)
        
        nextbutton = Button(root, text = "Next Question", command=self.nextbtn, highlightbackground = "#ccecf0")
        
        nextbutton.place(x=375,y=380)

        quitbutton = Button(root, text = "Quit", command = root.destroy, highlightbackground = "#ccecf0")
        
        #root.destroy means end the program.

        
        quitbutton.place(x=650,y=380)



    def checkans(self, qn):

        if self.opt_selected.get() == a[qn]:

             return True

    def nextbtn(self):

        if self.checkans(self.qn):

            self.correct += 1

        self.qn += 1

        if self.qn == len(q):

            self.display_result()

        else:

            self.display_options(self.qn)      


    def backbtn(self):
    
        self.qn -= 1

        if self.qn == len(q):
            
            self.display_result()

        else:
            self.display_options(self.qn)
        

        

    def display_result(self):

        score = int(self.correct / len(q) * 100)

        result = "Your Score: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "The number of correct answers you had: " + str(self.correct)

        wrong = "The number of incorrect answers you had: " + str(wc)

        mb.showinfo("Your Result", "\n".join([result, correct, wrong]))



quiz=Quiz()

root.mainloop





        

    
            

        
