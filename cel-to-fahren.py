# Convert Fahrenheit to celsius and vice versa

# Define global variables

celsius = 0
fahrenheit = 0


#
celsius = raw_input('Type in Celsius degrees:\n')

fahrenheit = float(9/5.0) * int(celsius) + int(32)
print
print "9/5.0 is:", float(9/5.0), "(only if you define it as a float)!"
print
print "*********************************************"
print int(celsius), "Degree Celsius", "is:", int(fahrenheit), "Fahrenheit degrees"
print "*********************************************" 
print