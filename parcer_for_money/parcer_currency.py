from scraper import *
from date_and_time_funcs import *

print('Приветствую тебя в парсере валют')
print("Подожди немного, я обновлю информацию")
# Получаем сырой html-код с сайта
html = get_html(URL)
print('Подключаюсь к базе Центробанка')
# Вытягиваем из страницы таблицу с валютами в виде кусков HTML-кода, возвращает объект BS
table = get_table(html)
print('Собираю данные')
#Вытягивает из таблицы список валют
data = get_data(table)
print('Формирую список валют')
# Формирует  список словарей, где данные о каждой валюте содержаться в словаре
currences = get_content(data)

#Формируем название файла

filename = get_filename()

# Записывает эти данные в CSV-файл
saving_as_csv(filename,headers,currences)
print("Все готово,можете ознакомиться с результатами, они сохранены в отдельный файл")
# Выводим сообщение о курсах основных валют
get_today_text()
get_main_courses(currences)

