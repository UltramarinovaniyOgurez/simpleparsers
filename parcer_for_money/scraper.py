import requests
from bs4 import BeautifulSoup as BS
import csv

# filename = 'currencies.csv'
HOST = 'https://www.cbr.ru/'
URL = "https://www.cbr.ru/currency_base/daily"
headers = ['Валюта',"Буквенный код",'Курс к рублю']

def get_html(URL):
    '''Получаем HTML-код всей страницы'''
    source = requests.get(URL).text
    return source

def get_table(source):
    '''Получает таблицу со страницы'''
    soup = BS(source,'lxml')
    table = soup.find('div', class_="table")
    return table

# def get_headers(table):
#     '''Получает заголовки из таблицы - Ненужная поебень'''
#     # source_headers = soup.find('tr').find_all('th')
#     source_headers = table.find('tr').find_all('th')
#     headers = [header.get_text() for header in source_headers]
#     return headers

def get_data(table):
    '''Получает данные о валютах из таблицы'''
    data = table.find_all('tr')
    del data[0]
    return data

def get_content(data):
    '''Заполняет список валют'''
    currences = []
    for item in data:
        currency_data  = item.find_all('td')
        currency = [row.get_text() for row in currency_data if row]
        formated_currency = {
            'name' : currency[3],
            'letter-code' : currency[1],
            'cuontity' : int(currency[2]),
            'price' : float(currency[-1].replace(',','.'))
        }
        currences.append(formated_currency)

    return currences


def saving_as_csv(filename, headers,currences):
    '''Сохраняет данные в файл-csv'''
    with open(filename,'w',encoding='utf-8-sig') as result:
        writer = csv.writer(result,delimiter=';')
        writer.writerow(headers)
        for currence in currences:
            if currence['cuontity'] == 1:
                row = [currence['name'],currence['letter-code'],currence['price']]
            else:
                row = [currence['name'],round(currence["price"]/currence['cuontity'],4)]
            writer.writerow(row)



# # Получаем сырой html-код с сайта
# html = get_html(URL)
# # Вытягиваем из страницы таблицу с валютами в виде кусков HTML-кода, возвращает объект BS
# table = get_table(html)
# #Вытягивает из таблицы список валют
# data = get_data(table)
# # Формирует  список словарей, где данные о каждой валюте содержаться в словаре
# currences = get_content(data)
# # Записывает эти данные в CSV-файл
# saving_as_csv(filename,headers,currences)