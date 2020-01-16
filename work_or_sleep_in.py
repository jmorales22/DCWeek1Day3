# This will prompt the user for a number between 0 and 6
# The output will be whether the user has to go to work or if they can sleep in

# This variable stores the number that the user enters once they are prompted
day = int(input("Day(0-6)"))
# The if statement will print out if the user enters 0 or 6, which is Saturday and Sunday
if day == 0 or day == 6:
    print("Sleep In")
# The else statement will print out go to work if the user enters any other number besides 0 and 6
else:
    print("Go to work")