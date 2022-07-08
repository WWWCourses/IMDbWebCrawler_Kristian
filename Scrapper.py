from bs4 import BeautifulSoup as bs
# from html_parser import html
import requests


class Scraper:
    def __init__(self, html):
        self.html = html
        self.soup = bs(html, 'html.parser')

    # def get_film_ratings(self):
    #     for row in self.soup.select('tbody tr'):
    #         for x in row.find_all('strong'):
    #             rate = float(x.get_text())
    #             return rate

    def get_movies_urls(self,min_rating):
        # get all movies info rows from 'tbody.lister-list'
        rows = self.soup.select('tbody.lister-list tr')

        # the list into which relevat movies urls will be stored:
        movies_urls = []

        for row in rows:
            # get IMDB rating value - the content of strong element which is in td.imdbRating
            rating_element = row.select_one('td.imdbRating strong')
            if rating_element:
                rating = float(rating_element.get_text())

                if rating>min_rating:
                    # get movie url:
                    movie_url = row.select_one('td.titleColumn a')['href']
                    movies_urls.append(movie_url)

        return movies_urls


    def get_into_movie_title(self):
        urls = list()
        base_url = 'https://www.imdb.com'
        for td in self.soup.find_all('td', class_='titleColumn'):
            for link in td.find_all('a'):
                url = base_url + link.get('href')
                r = requests.get(url)
                if r.ok:
                    new_soup = bs(r.text, 'html.parser')
                    rate = new_soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').get_text()
                    rating = float(rate)
                    print(rating)
                    if rating >= 8.0:
                        urls.append(url)

        return urls
