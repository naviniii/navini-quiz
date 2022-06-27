#This is my first version of the quizbot program.
#I will be writing the programming for my first component: Asking for user details
#This will be text-based originally, and in the second version I will make it GUI

#The starting words:
print("Hello! Welcome to the General Knowledge Quiz!")
print("You will be required to enter your name, age and year level")
print("You must be atleast 12-18 years old in age")

#Asking for user details:

while True:
    name = input("What is your name: ")
    name = name.title()

    if name.isalpha():
        break

    else:
        print("Please use only letters to write your name")

while True:
    try:
        age = int(input("How old are you: "))

    except ValueError:  
        print("Please only use numbers to write your age")
        continue

    if age <= 18 and age >= 12:
        break

    else: 
        print("You must be between 12-18!")


print("Hello {}! So nice to meet you!".format(name))


