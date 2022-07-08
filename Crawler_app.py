from re import M
import requests
from Scrapper import Scraper


class Crawler:
    def __init__(self, url, base_url):
        self.url = url
        self.base_url = base_url

    def start(self):
        # get main page html
        html = self.get_html(self.url)
        self.save_html(html, 'imdb.html')

        # get movies urls, which rating is bigger than 8
        self.movies_urls = self.get_movies_urls(min_rating=8)
        print(self.movies_urls)

        # TODO: from each url in movies_url get movie info

    def get_movies_urls(self, min_rating):
        html = self.get_html(self.url)
        scraper = Scraper(html)

        movies_urls = scraper.get_movies_urls(min_rating)
        # prepend base_url to each element in movies urls:
        movies_urls = [self.base_url+url for url in movies_urls]
        return movies_urls

        # TODO:


    def get_html(self, url):
        try:
            r = requests.get(url)
        except Exception as e:
            print(f'Can not get url: {url}: {str(e)}!')
            exit(-1)

        r.encoding="utf-8"

        # if we have repsonse => get and return html content
        if r.ok:
            html = r.text

        return html

    def save_html(self, content, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)


if __name__ == '__main__':
    craw = Crawler( url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm',
                    base_url = 'https://www.imdb.com'
    )
    craw.start()
