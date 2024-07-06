import requests
from bs4 import BeautifulSoup as BS
import csv


CSV = 'cards.csv'
HOST = 'https://arbuz.kz/'
URL = 'https://arbuz.kz/ru/almaty/catalog/cat/225172-kofe_i_kakao#/'
HEADRES = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}


def get_html(url,params = ''):
    '''Получаем html-код страницы по указанному URL-адресу'''
    request = requests.get(url,headers=HEADRES,params=params)
    return request


def get_content(html):
    '''Отбирает нужные данные (Название, ссылку, цену, изображение) для каждого товара со страницы'''
    soup = BS(html, 'lxml')
    items = soup.find_all('article',class_="product-item product-card")
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find("a", class_="product-card__link").get("title"),
                'link_to_product': HOST + item.find("a", class_="product-card__link").get('href'),
                "price" : item.find("p", class_="product-card__price").get_text().strip(),
                'card_img':HOST + item.find('a',class_="product-card__link").find('img',class_="product-card__img").get('src')
            }
        )

    return cards

def save_doc(items,path):
    '''сохраняет днв csv-файл'''
    # Важный момент - использование кодировки 'utf-8-sig' для корректного отображения кириллицы в эксель
    with open(path,'w',encoding='utf-8-sig',newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название','Ссылка','Цена','Ссылкана изображение'])
        for item in items:
            writer.writerow([item['title'],item['link_to_product'],item["price"],item['card_img']])

def parser():
    PAGENATION = int(input("Кол-во страниц для парсинга:").strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1,PAGENATION+1):
            print(f'Парсим страницу{page}')
            html = get_html(URL,params={"value": f'%3A{page}'})
            content = get_content(html.text)
            cards.extend(content)
    else:
        print("Ошибка на той стороне")
    return cards

items = parser()
save_doc(items,CSV)

#  Тест для проверки результатов скрэпинга и парсинга
# html = get_html(URL)
# content = get_content(html.text)
# print(content)