from scraper import *
# Получаем сырой html-код с сайта
html = get_html(URL)
# Вытягиваем из страницы таблицу с валютами в виде кусков HTML-кода, возвращает объект BS
table = get_table(html)
#Вытягивает из таблицы список валют
data = get_data(table)
# Формирует  список словарей, где данные о каждой валюте содержаться в словаре
currences = get_content(data)

courses = get_main_courses(currences)
for k,v in courses.items():
    print(f'{k} - {v}')


