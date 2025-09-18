import requests
from bs4 import BeautifulSoup


search_term = input("Enter your search term: ")

response = requests.get("https://digiato.com/", params={"s": search_term})

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a", class_="rowCard__title")

for title in titles:
    print(f"Title: {title.get_text(strip=True)}")
    print(f"URL: {title.get("href")}\n")
