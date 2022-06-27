#this program is the quiz-component of my program


#exporting tkinter from external library
from tkinter import *
from tkinter import messagebox as mb #importing messagebox for the end of quiz score


#questions of my program. These are stored in a list variable: "q"
q=["question 1",
   "question 2",
   "question 3",
   "question 4",
   "question 5"]

#the multi-choice options of my program. These are stored in the list called: "options"
options=[
    ['answer a', 'answer b', 'answer c','answer d'],
    ['answer a', 'answer b', 'answer c','answer d'],
    ['answer a', 'answer b', 'answer c','answer d'],
    ['answer a', 'answer b', 'answer c','answer d'],
    ['answer a', 'answer b', 'answer c','answer d'],
    ]

#the answers to the questions. These are stored in the list called: "a"
a=[3,4,1,3,2]



#starting the program
#to run the window called root
root = Tk()

#the size of the window
root.geometry("800x500")

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

        t = Label(root, text="General Knowledge Quiz")

        t.place(x=5, y=5)

        qn = Label(root, text=q[qn])

        qn.place(x=70, y=100)

        return qn


    

#the radio buttons on the questions.

    def radiobtns(self):

        val = 0

        b = []

        yp = 150

        while val < 4:

            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1)

            b.append(btn)

            btn.place(x=100, y=yp)

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
        
        nbutton = Button(root, text = "Next Question :) ", command=self.nextbtn)
        
        nbutton.place(x=200,y=380)

        quitbutton = Button(root, text = "Quit :(", command = root.destroy)
        
        #root.destroy means end the program.

        
        quitbutton.place(x=380,y=380)



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


            

    def display_result(self):

        score = int(self.correct / len(q) * 100)

        result = "Your Score: " + str(score) + "%"

        wc = len(q) - self.correct

        correct = "The number of correct answers you had: " + str(self.correct)

        wrong = "The number of incorrect answers you had: " + str(wc)

        mb.showinfo("Your Result", "\n".join([result, correct, wrong]))


quiz=Quiz()

root.mainloop





        

    
            

        
