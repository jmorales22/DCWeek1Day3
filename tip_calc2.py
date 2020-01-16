# This will promp the user to enter a bill amount
# In a second prompt, the user will be asked for the level of service
# In the third prompt, the user will be asked how many ways the bill should be split

# This prompts the user to enter the total bill amount
# It returns the number as a float
amount = float(input("What is the total bill amount? "))

# This prompts the user to enter the type of service received
# This prompt will determine the amount of tip the server has earned
service = input("What was the level of service? good, fair, or bad? ")

# This was written in case the user does not enter all lower case
service_lower = service.lower()

# This will prompt the user to enter the number of ways the bill should be split
split = int(input("Split how many ways? "))

# This if statement returns the tip, total bill amount if the service was good
# It also divides the amount by the number of people
if service_lower == "good":
    var_tip1 = float(0.2*amount)
    var_total1 = float(var_tip1 + amount)
    per_person1 = float(var_total1/split)
    print("Tip amount: " + str('%.2f' % var_tip1))
    print("Total amount:" + str('%.2f' % var_total1))
    print("Amount per person: " + str('%.2f' % per_person1))
# This if statement returns the tip, total bill amount if the service was fair
# It also divides the amount by the number of people
elif service_lower == "fair":
    var_tip2 = float(0.15*amount)
    var_total2 = float(var_tip2 + amount)
    per_person2 = float(var_total2/split)
    print("Tip amount: " + str('%.2f' %var_tip2))
    print("Total amount:" + str('%.2f' %var_total2))
    print("Amount per person: " + str('%.2f' % per_person2))
# This else statment covers bad service and is the default for any bad entries that may have been made
# It als divides the amount by the number of people
else:
    var_tip3 = float(0.1*amount)
    var_total3 = float(var_tip3 + amount)
    per_person3 = float(var_total3/split)
    print("Tip amount: " + str('%.2f' %var_tip3))
    print("Total amount:" + str('%.2f' %var_total3))
    print("Amount per person: " + str('%.2f' % per_person3))