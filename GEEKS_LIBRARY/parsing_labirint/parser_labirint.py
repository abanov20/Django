import requests
from bs4 import BeautifulSoup as BS4
from django.template.defaultfilters import title
from urllib3 import request

URL = 'https://www.labirint.ru'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
}

#start
def get_html(url, params=""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#get data
def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all('div', class_='genres-carousel__container products-row')
    labirint_list = []
    for item in items:
        title = item.find('span', class_='product-title').get_text(strip=True)
        image = item.find('img').get('data-src')
        if image:
            image = URL + image
        labirint_list.append({
            'title': title,
            'image': image
        })
    return labirint_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        labirint_list2 = []
        for page in range(1, 2):
            response = get_html("https://www.labirint.ru/books/", params={'page': page})
            labirint_list2.extend(get_data(response.text))
        return labirint_list2
    else:
        raise Exception('Error Parsing labirint')
print(title)