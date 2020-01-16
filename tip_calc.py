# This will promp the user to enter a bill amount
# In a second prompt, the user will be asked for the level of service


# This prompts the user to enter the total bill amount
# It returns the number as a float
amount = float(input("What is the total bill amount? "))

# This prompts the user to enter the type of service received
# This prompt will determine the amount of tip the server has earned
service = input("What was the level of service? good, fair, or bad? ")
# This was written in case the user does not enter all lower case
service_lower = service.lower()
# This if statement returns the tip and total bill amount if the service was good
if service_lower == "good":
    var_tip1 = float(0.2*amount)
    var_total1 = float(var_tip1 + amount)
    print("Tip amount: " + str('%.2f' % var_tip1))
    print("Total amount:" + str('%.2f' % var_total1))
# This if statement returns the tip and total bill amount if the service was fair
elif service_lower == "fair":
    var_tip2 = float(0.15*amount)
    var_total2 = float(var_tip2 + amount)
    print("Tip amount: " + str('%.2f' %var_tip2))
    print("Total amount:" + str('%.2f' %var_total2))
# This else statment covers bad service and will also be the default option
else:
    var_tip3 = float(0.1*amount)
    var_total3 = float(var_tip3 + amount)
    print("Tip amount: " + str('%.2f' %var_tip3))
    print("Total amount:" + str('%.2f' %var_total3))

