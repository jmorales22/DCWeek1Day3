#This script is set up like a madlib
#The user will be prompted to give a name and a favorite subject
#There will be 3 print functions used

#The matlib variable tells the user what they will be doing 
madlib = input("Please fill in the blanks below: ")
#The print function will show the user the blanks they need to fill in
print("____(name)_____'s favorite subject in school is _____(subject)_____.")
#The name variable will prompt and store the name entered by the user
name = input("What is name? ")
#The subject variable will prompt and store the subject entered by the user
subject = input("What is subject? ")
#The print function will apply the answers supplied by the user into the madlib
print(name + "'s favorite subject in school is " + subject)