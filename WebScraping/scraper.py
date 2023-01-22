import requests
from bs4 import BeautifulSoup

# sending a request to the particular website.
req = requests.get("https://pip.pypa.io/en/stable/installation/");

# beautiful soup on the response for the request of html part
soup = BeautifulSoup(req.content, "html.parser")

# printing the title of the website
print(soup.title.get_text())

# creating and adding the data of beautifulsoup in the text file.
f = open('text1.txt', 'w+')
f.write(soup.prettify())
f.close()

print('Program Completed 🐍')