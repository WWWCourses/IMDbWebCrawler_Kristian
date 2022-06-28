import requests
from Scrapper import Scraper


class Crawler:
    def __init__(self, url):
        self.url = url

    def start(self):
        html = self.get_url()
        self.save_html(html, 'imdb.html')
        scraper = Scraper(html)
        urls = scraper.get_into_movie_title()
        urls = [base_url + url for url in urls]
        print(urls)
        best_urls = scraper.get_film_links()
        print(best_urls)

    def get_url(self):
        r = requests.get(self.url)
        if r.ok:
            return r.text

    def save_html(self, content, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)


if __name__ == '__main__':
    base_url = 'https://www.imdb.com'
    craw = Crawler('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm')
    craw.start()
