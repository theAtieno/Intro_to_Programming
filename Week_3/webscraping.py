import requests
from bs4 import BeautifulSoup

# html = """
# <html>
#   <body>
#     <h1>Main Title of the Page</h1>
#     <h2>Subheading 1</h2>
#     <p class="intro">Welcome to the website!</p>
#     <p>Here is some more text.</p>
#     <a href="https://example.com">Visit Example</a>
#     <img src="image.jpg" alt="Sample Image">
#     <ul>
#       <li>Item One</li>
#       <li>Item Two</li>
#     </ul>
#   </body>
# </html>
# """
# soup = BeautifulSoup(html, "html.parser")

# heading = soup.find("h1")
# intro_para = soup.find("p", class_="intro")
# first_link = soup.find("a")
# first_image = soup.find("img")

# print("First heading:", heading.text)
# print("Intro paragraph:", intro_para.text)
# print("First link URL:", first_link['href'])
# print("First image source:", first_image['src'])

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Fetched successfully")

else:
    print(f"Error: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

# one1 = soup.find("div", class_ = "quote")
# print(one1)

one = soup.find("div", class_ = "tags")
# print(one)

# for i in one:
#     print(one.text)

# links = one.find_all("a", class_ = "tag")
# print(links)

# for i in links:
#     print(i.text)
#     # print(i['href'])

# quotes = soup("span", class_ = "text")
# for i in quotes:
#     print(i.text)

authors = soup("small", class_ = "author")
for i in authors:
    print(i.text)
