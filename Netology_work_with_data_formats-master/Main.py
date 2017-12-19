import json
from pprint import pprint
import chardet


def words_count(items):  # Считаем кол-во слов в списке всех новостей
    words = {}
    for new in items:
        new_text = new['description'].split()

        for word in new_text:
            if word in words:
                words[word] += 1
            elif len(word) > 6:
                words[word] = 1

    return words


def find_top_words(word_count):  # Находим 10 наиболее часто встречающихся слов

    top_words_list = sorted(word_count.items(), key=lambda item: item[1])
    top_words_list = list(reversed(top_words_list))

    return top_words_list[:10]


def json_load(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        file_encoding = chardet.detect(data)
        data = data.decode(file_encoding['encoding'])
        data = json.loads(data)
    items = data['rss']['channel']['items']

    return items


filenames = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

for filename in filenames:
    items = json_load(filename)
    items = words_count(items)

    top_words = find_top_words(items)

    print('filename %s:' % filename)
    pprint(top_words)
    print('\n')
