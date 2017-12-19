import requests
import os


def translate_text(text, pair):
    API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    API_KEY = 'trnsl.1.1.20171114T034050Z.3cb76c4f8d9fcc8a.952632f63a27775ff177162758a98667f1bf1fb6'

    response = requests.post(
        API_URL,
        params={
            'key': API_KEY,
            'lang': pair
        },
        data={
            'text': text
        }
    )

    answer = ''.join(response.json()['text'])

    return answer


def get_lang_list():
    API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'
    API_KEY = 'trnsl.1.1.20171114T034050Z.3cb76c4f8d9fcc8a.952632f63a27775ff177162758a98667f1bf1fb6'

    response = requests.post(
        API_URL,
        params={
            'key': API_KEY
        }
    )

    return response.json()['dirs']


def read_paths():
    default_path = os.getcwd()

    #  Чтение пути к входному файлу
    input_path = input('Введите путь к файлу с текстом: ')
    if input_path:
        while not os.path.exists(input_path):
            input_path = input('Путь не существует, введите корректный путь: ')

    output_default_filename = input_path.replace('.', '_translated.')

    # Чтение пути к выходному файлу
    output_filename = input('Введите имя выходного файла: ')
    if not output_filename:
        output_filename = output_default_filename

    output_path = input('Введите путь к выходному файлу: ')
    if output_path:
        while not os.path.exists(input_path):
            output_path = input('Путь не существует, введите корректный путь: ')

    output_path = os.path.join(output_path, output_filename)

    return input_path, output_path


def read_langs(lang_list):
    # Считывание входного языка
    input_lang = input('Введите язык, с которого нужно перевести (в кратком формате, например: "de", "en", "ru"): ')
    # Считывание выходного языка
    output_lang = input('Введите язык, на который нужно перевести (в кратком формате, например: "de", "en", "ru"): ')

    pair = input_lang + '-' + output_lang
    while pair not in lang_list:
        print('Произошла ошибка, данное направление перевода отсутствует, повторите ввод')
        # Считывание входного языка
        input_lang = input(
            'Введите язык, с которого нужно перевести (в кратком формате, например: "de", "en", "ru"): ')
        # Считывание выходного языка
        output_lang = input(
            'Введите язык, на который нужно перевести (в кратком формате, например: "de", "en", "ru"): ')
        pair = input_lang + '-' + output_lang

    return pair


def source_data_read():
    source = dict()
    lang_list = get_lang_list()
    source['input path'], source['output path'] = read_paths()
    source['lang pair'] = read_langs(lang_list)

    return source


def translate():
    source = source_data_read()
    with open(source['input path'], 'r') as in_file:
        input_text = in_file.read()

    output_text = translate_text(input_text, source['lang pair'])
    with open(source['output path'], 'w') as out_file:
        out_file.write(output_text)

    return 'Готово'


print(translate())