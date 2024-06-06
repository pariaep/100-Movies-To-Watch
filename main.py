import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
titles = soup.find_all("h3", class_="title")
title_texts = []
for title in titles:
    title_text = title.getText()
    title_texts.append(title_text)

sorted_list = title_texts[::-1]

with open("./movie.txt", "w") as file:
    for movie in sorted_list:
        file.write(f"{movie}\n")




