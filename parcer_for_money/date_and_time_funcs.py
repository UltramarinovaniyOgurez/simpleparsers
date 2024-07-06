from datetime import datetime as dt
import locale

locale.setlocale(locale.LC_TIME,'ru')

TIME_FORMAT = '%H:%M %d %B %Y'


def get_today_text():
    '''Получает текущую дату и время и форматирует их в строку'''
    moment = dt.today()
    text_time = moment.strftime(TIME_FORMAT)
    text = f'Курсы валют на {text_time}'
    return text

def get_filename():
    '''Формирует название файла'''

    name = dt.today().strftime('%d %B %Y')
    return f'Курсы валют на {name}.csv'

