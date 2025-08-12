# Exercises
# Write a program that generates a random number between 1 and 100. The user has to guess the number in a limited number of attempts. Provide feedback after each guess (higher, lower, or correct).
import random
random_number = random.randint(1,100)

# setting number of attempts
max_attempts = 4
attempts = 0

print("Guess the number between 1 and 100. You have" , max_attempts , "tries")

while attempts < max_attempts :
    guess = int(input("Enter your guess: "))
    attempts +=1

    if guess < random_number :
        print("Higher")
    elif guess > random_number :
        print("Lower")
    else :
        print("Correct")
        break
else :
    print("No more attempts left")




# Write a program that allows the user to enter two numbers and an operator (+, -, *, /) and perform the corresponding calculation. Use conditional statements to handle different operators
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

operator = input("Enter an operator( +, -, *, / ): ")

if operator == "+" :
    z = x + y
    print(z)
elif operator == "-" :
    z = x -y
    print(z)
elif operator == "*" :
    z = x * y
    print(z)
else :
    z = x/y
    print(z)



# Write a program that uses a while loop to check if a number entered by the user is a prime number (divisible only by 1 and itself).
x = int(input("Enter a number: "))

if x <= 1 :
    print("x is not a prime number")
else :
    divisor = 2
    is_prime_number = True

    while divisor < x:
        if x % divisor == 0 :
            is_prime_number = False
            break
        divisor += 1
    if is_prime_number :
        print("x is a prime number")
    else :
        print("x is not a prime number")



# Write a program that uses a for loop to print the multiplication table of a number entered by the user (up to a specified number of multiples).
x = int(input("Enter a number: "))
multiples = int(input("Enter how many multiples: "))
multiples = 5
for i in range(1 , multiples + 1) :
    print(x, "*", i, "=", x * i)



# Write a program that uses a for loop to calculate the sum of numbers from 1 to a given number entered by the user.
x = int(input("Enter a number: "))
sum = 0
for i in range(1 , x+1) :
    sum +=i
print("Sum of numbers from 1 to", x, "is", sum)


# Write a program that uses a for loop to print a pattern of stars or characters like a triangle.
x = int(input("Enter a number: "))
for i in range(1, x+1):
    print(i * "<>")