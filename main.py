import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
empire_web = response.text

soup = BeautifulSoup(empire_web, "html.parser")

goat = soup.find_all(name="h3", class_="title")

goat_movie_list = [movie.getText() for movie in goat]

rgoat_movie_list = goat_movie_list[ : :-1]

with open("movies.txt", "a", encoding="utf-8") as file:
    for movie in rgoat_movie_list:
        file.write(f"{movie}\n")

# for movie in goat:

# print(goat_movie_list)
# print(type(goat_movie_list))
# print(rgoat_movie_list)
