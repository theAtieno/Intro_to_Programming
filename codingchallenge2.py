# Create a function that will determine whether a number is positive or negative.
def check_number(num):
    if num > 0:
        print("positive")
    elif num <0 :
        print("negative")
    else:
        print("num is zero")
number = float(input("Enter a number: "))
check_number(number)

# Write functions to calculate the area of different shapes like square (area_of_square(side_length)), rectangle (area_of_rectangle(length, width)), and circle (area_of_circle(radius)).
def area_of_square(side_length):
    return side_length * side_length

def area_of_rectangle(length, width):
    return length * width

def area_of_circle(radius):
    pi = 3.142
    return pi * radius * radius

shape = input("Enter shape(square/rectange/circle): ")

if shape == "square":
    side = float(input("Enter length of side: "))
    print("Area of square" , area_of_square(side))

elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle" , area_of_rectangle(length, width))
else:
    radius = float(input("Enter the radius: "))
    print("Area of circle" , area_of_circle(radius))
              


# Write a function called calculate_grade that takes a score as input and returns the corresponding letter grade (A, B, C, D, F) based on a grading scale (e.g., A: 90-100, B: 80-89, etc.).
def calculate_grade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score >= 50:
        print("E")
    else:
        print("F")
grade = float(input("Enter a score: "))
calculate_grade(grade)

