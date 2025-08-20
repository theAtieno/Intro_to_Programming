import re

# text = "aab a1b acd cba aac dcd"
# pattern = r"a*b"

# matches = re.findall(pattern, text)
# print(matches)

# text = "cat scatter category"

# pattern = "cat"

# match = re.findall(pattern, text)
# print(match)

# pattern = r"\bcat\b"

# match = re.findall(pattern, text)

# print(match)


# pattern = r"\Bscatter\b"

# match = re.findall(pattern, text)

# print(match)

# text = "I am a 3good teacher"

# pattern = r"\Bgood\b"

# match = re.findall(pattern, text)

# print(match)

# # fnd words starting with

# text = "apython is fun and mypython py programming is py"

# pattern = r"\w*py\w*"

# match = re.findall(pattern, text)

# print(match)

# text = "apython is fun and python bpy pyprogramming is py"

# pattern = r"\bpy\w*\b"

# match = re.findall(pattern, text)

# print(match)

# text = "Hello world, I am Atieno"

# pattern = r"\w*[oe]\w*"

# match = re.findall(pattern, text)

# print(match)

# text = "Hello world, I am Atieno"

# pattern = r"\w*[a-z]\w*"

# match = re.findall(pattern, text)

# print(match)

# text = "Hello world, I am Atieno"

# pattern = r"\w*[B]\w*"

# match = re.findall(pattern, text)

# print(match)

# # find all digit numbers

# number = "My number is 250 793-123457"

# pattern = r"\d{3}\s\d{3}-\d{6}"

# match =re.findall (pattern, number)

# print(match)

# number = "My number is 250 793-123457"

# pattern = r"(\d{3})\s(\d{3}-\d{6})"

# # #search

# match =re.findall(pattern, number)

# print(match)

# # group
# pattern = r"(\d{3})\s(\d{3}-\d{6})"

# #use search

# match =re.search(pattern, number)
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))

# number = "250 793-123457 , 254 791-123654 , 256 780-654321"

# pattern = r"\d{3})(\s(\d{3}-\d{6})"

# # #use search

# match = re.search(pattern, number)
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))

# text = f"""
# My email is user@example.com, or 
# contact@domain.com"""

# pattern = r"\b[a-z]+@+[a-z]+\.com\b"

# match =re.findall(pattern, text)

# print(match)

# email = f""" atieno@yahoo.com, mercy@org.com , BERN@nhif.com , nerd@gmail.com"""

# pattern = r"\b[a-z]{4}+@+[a-z]+\.com\b"

# match =re.findall(pattern, email)

# print(match)

email = f""" atieno@yahoo.com, mercy@org.com , BERN@nhif.com , nerd@gmail.com"""

pattern = r"\b\w*{25}\d\.\#\_[@]\w*\.{10}" 

match =re.findall(pattern, email)

print(match)