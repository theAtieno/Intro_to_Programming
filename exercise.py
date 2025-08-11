# Exercise 1: Write a program that uses input to prompt a user for their name and then welcomes them.
name = input(" Enter your name: ")
greeting = "Hello "

print(greeting + name)

# Exercise 2: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = float(input("Enter a decimal number: "))
rate = float(input("Enter a decimal number: "))
pay = hours * rate

print(pay)

# Exercise 3: Assume that we execute the following assignment statements:
width = 17
height = 12.0

# For each of the following expressions, write the value of the expression and the type (of the value of the expression).

# width//2
x = width//2

print(x)
print(type(x))

# width/2.0
x = width/2.0

print(x)
print(type(x))

# height/3
x = height/3

print(x)
print(type(x))

# 1 + 2 * 5
x = 1 + 2 * 5

print(x)
print(type(x))


# Exercise 4: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
celcius = float(input("Enter temperature in celcius: "))

fahrenheit = celcius * 9/5 + 32

print(fahrenheit)