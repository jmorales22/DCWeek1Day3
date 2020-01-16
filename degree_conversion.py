# The user will be prompeted to enter a temperatures in degrees Celsius
# The output will be the temperature converted into degrees Fahrenheit

# This will prompt the user to enter a temperature in degrees Celcius
# It will store the temperature in the temp variable
temp = int(input("What is the temperature in degrees Celcius? "))
# The deg_f variable stores the conversion of the temperature that was entered above
deg_f = temp*1.8 + 32
# The print function prints out the temperature in degrees Fahrenheit
# Using the interpolation operator limits the decimal place to 2
print(str('%.2f' % deg_f) + " F")