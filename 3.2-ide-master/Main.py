import chardet


def words_count(news):
    words_count_tmp = {}
    for item in news:  # считаем количество слов и записываем все в словарь
        words_list_tmp = item.split()

        for word in words_list_tmp:
            if word in words_count_tmp:
                words_count_tmp[word] += 1
            elif len(word) > 6:
                words_count_tmp[word] = 1

    return words_count_tmp


def print_top_words(filename, word_count):
    word_count = sorted(word_count.items(), key=lambda item: item[1])
    word_count = list(reversed(word_count))

    print('filename ', filename, ': ')
    for j in range(10):
        print('\t', word_count[j][0], ' - ', word_count[j][1])


def top_words_find(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data.strip()
        news = data.split('\n')
        news = [new.strip() for new in news]

    word_count = words_count(news)
    print_top_words(filename, word_count)


filenames = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']

for filename in filenames:
    top_words_find(filename)