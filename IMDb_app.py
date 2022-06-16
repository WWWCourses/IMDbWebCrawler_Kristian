import requests


def save_html(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


base_url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

r = requests.get(base_url)
print(r.status_code)

save_html(r.text, 'imdb.html')
