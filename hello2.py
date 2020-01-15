# User will be prompted to enter name
# The terminal will print out hello plus their name in caps
# The terminal will print how many letters is in the name

#This will prompt the user to enter their name
name = input("What is your name? ")
# These are three variables created to give the proper output
hello_output = "Hello " + name + "!"
name_length = len(name)
name_length_output = "Your name has " + str(name_length) + " letters in it! Awesome!"
#Use the print function to output Hello plus name in all caps
print(hello_output.upper())
#Use the print function to output how many letters the name has
print(name_length_output.upper())