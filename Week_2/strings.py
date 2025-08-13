name = "Hello World"
print(name.split)

name = "Atieno"
school = "Zindua"

print(f"My name is {name} and I go to {school} School")

for i in name:
    print(i)

# print(len(name))

txt = "I am alive"
print("alive" in txt)
print("alive not in txt")

file = open(r"/Users/atienojacinta/Introduction to Programming/Week_2/quotes.txt" , "r")

content = file.read()

print(content)

file.close()

# with statement
with open(r"/Users/atienojacinta/Introduction to Programming/Week_2/quotes.txt" , "r") as file:
    
    content = file.read()
    
    print(content)

with open(r"/Users/atienojacinta/Introduction to Programming/Week_2/quotes.txt" , "r") as file:
    
    content = file.readline()
    
    print(content)

with open(r"/Users/atienojacinta/Introduction to Programming/Week_2/quotes.txt" , "r") as file:
    
    content = file.readlines()

    print(content)

with open(r"/Users/atienojacinta/Introduction to Programming/Week_2/quotes.txt" , "r") as file:
    
    content = file.readlines()

    print(content[0])

    print(content[1])

    print(content[2])

# append an existing file

with open(r"/Users/atienojacinta/Introduction to Programming/Week_2/quotes.txt" , "a") as file:
    file.write("\nThe end justifies the means -Atieno")

with open(r"/Users/atienojacinta/Introduction to Programming/Week_2/proverbs2.txt" , "w") as file:
   
    file.write("Hello")

import os

old_file = "proverbs2.txt"
new_file = "proverbs2.py"

os.rename (old_file, new_file)

old_file = "proverbs2.py"
new_file = "lists.py"

os.rename (old_file, new_file)

import os

file_name = "tuples2.py"

with open(file_name, "w") as f:
    pass

import os
os.remove("tuples2.py")
