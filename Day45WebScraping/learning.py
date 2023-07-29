from bs4 import BeautifulSoup
import requests


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.find_all("a"))

print(soup.find(name="h1", id="name"))
print(soup.find(name="h3", class_="heading"))

print(soup.select_one("p a"))
print(soup.select(".heading"))

for tag in soup.find_all("a"):
    print(tag.getText())
    print(tag.get("href"))
