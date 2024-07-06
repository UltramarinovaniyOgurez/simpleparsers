import requests
from bs4 import BeautifulSoup as BS
import csv

# filename = 'currencies.csv'
HOST = 'https://www.cbr.ru/'
URL = "https://www.cbr.ru/currency_base/daily"
headers = ['Количество','Валюта','Курс к рублю']

def get_html(URL):
    '''Получаем HTML-код всей страницы'''
    source = requests.get(URL).text
    return source

def get_table(source):
    '''Получает таблицу со страницы'''
    soup = BS(source,'lxml')
    table = soup.find('div', class_="table")
    return table



def get_data(table):
    '''Получает данные о валютах из таблицы'''
    data = table.find_all('tr')
    del data[0]
    return data

def get_content(data):
    '''Заполняет список валют'''
    currences = {}
    for item in data:
        currency_data  = item.find_all('td')
        currency = [row.get_text() for row in currency_data if row]
        letter_code = currency[1]
        currences[letter_code] ={
                'name' : currency[3],
            'quontity' : int(currency[2]),
            'price' : float(currency[-1].replace(',','.'))
             }
    return currences


def saving_as_csv(filename, headers,currences):
    '''Сохраняет данные в файл-csv'''
    with open(filename,'w',encoding='utf-8-sig') as result:
        writer = csv.writer(result,delimiter=';')
        writer.writerow(headers)
        for currence in currences.keys():
            current = currences[currence]
            row = [current['quontity'], current['name'], current['price']]
            writer.writerow(row)

def get_main_courses(currences):

    courses = {
        'USD' : currences['USD']['price'],
        'EUR' : currences['EUR']['price'],
        'CNY' : currences['CNY']['price']
    }
    for k, v in courses.items():
        print(f'{k} - {v}')
