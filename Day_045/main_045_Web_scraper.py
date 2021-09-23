import bs4
import requests


url_to_scrape = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
movies = list()
final_list = list()


def scrape_site():
    response = requests.get(url=url_to_scrape)
    timeout_page = response.text
    soup = bs4.BeautifulSoup(timeout_page, "html.parser")
    hits = [hit.getText() for hit in soup.find_all(name="h3", class_="_h3_cuogz_1")]
    for title in hits[:-1]:
        movies.append(title.split("\xa0"))
    for title in movies:
        final_list.append(title[0] + title[1])


def save_to_file():
    with open("100_top_movies.txt", mode="w") as file:
        for movie in final_list:
            file.write(movie + "\n")


def main():
    scrape_site()
    save_to_file()

if __name__ == "__main__":
    main()
