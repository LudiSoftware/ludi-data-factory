import requests
from bs4 import BeautifulSoup

url = "https://www.birminghamunited.com/coaches/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the container with the list of coaches
coaches_container = soup.find("div", class_="et_pb_text_inner")

# Extract the text of each coach's name
coaches = [coach.text for coach in coaches_container.findAll("p")]

print(coaches)