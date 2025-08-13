name = "Atieno"

print (name)

print ("Hello World")

name = "Atieno"
age = 25
height = 1.57

print(name)
print(age)
print(height)

# contants don't change 
# variales are in caps


PI = 3.142
print(PI)

#python expressions; vales, variables, operators

x = 10
y = 12

print(x+y)

z = x + y

print(z)

greeting = "Hey hey"
name = " Atieno"

# print(greeting + name)

intro = (greeting + name)

print(intro)

wine = input()
print("Wine is", wine)

print(type(wine))

age = input("Enter your age : ")
print(int(age))
print(type(age))

age = input("what is your age ")
age = int(age)

if age < 18:
    print("St. Patrick day")
else:
    print("minor")

if age < 18:
    print("Minor")
elif age <=21:
    print("Young adult")
else:
    print("adult")

x = 50
if x < 2 :
    print("Small")
elif x < 10:
    print("Medium")
print("All done")

n = 5
while n > 0 :
    print(n)
    n = n - 6
print("Blastoff")
print(n)

name = "Atieno"
school = "Zindua"

print(f"My name is {name} and I go to {school} School")

for i in name:
    print(i)

print(len(name))

txt = "I am alive"
print("alive" in txt)
print("alive not in txt")


