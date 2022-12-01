import requests
from bs4 import  BeautifulSoup as BS
import  csv

order=input('введите ваш поиск: ')
url='https://www.avito.ru/moskva?q='+order
req=requests.get(url)

with open(f"{order}.html", 'w', encoding='utf-8') as file:
    file.write(req.text)
with open(f"{order}.html",  encoding='utf-8') as file:
    html=file.read()

soup=BS(html, 'html.parser')

names_links=soup.findAll('div', class_='iva-item-titleStep-pdebR')
prices=soup.findAll('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL')
images=soup.findAll('div', class_='photo-slider-item-nKXVO photo-slider-keepImageRatio-C5mWU')

with open(f"{order}.csv", 'a', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(
        (
            'Имя',
            'Ссылка',
            'Цена',
            'Ссылка на изо.'
        )
    )
    for i in range(len(names_links)):
        name=names_links[i].text
        link=names_links[i].find('a').get('href')
        price=prices[i].text
        image=images[1].find('img').get('src')

        writer.writerow(
            (
                name,
                link,
                price,
                image
            )
        )

