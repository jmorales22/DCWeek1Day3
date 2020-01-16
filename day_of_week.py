# This will prompt the user to choose a number between 0 and 6
# Each number is assigned to a day of the week
# Sunday is zero, Monday is one, Tuesday is two, etc.

# This variable will store the number that the user has entered
day = int(input("Day (0-6)?"))
# Each if and elif statement determines which day will be returned to the console
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Saturday")

