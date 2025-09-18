import requests

search_term = input("Enter your search term: ")

response = requests.get("https://digiato.com/", params={"s": search_term})

if response.status_code == 200:
    print(response.text)
