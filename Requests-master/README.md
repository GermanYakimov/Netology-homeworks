# Requests

При запуске программа считывает следующие данные: путь к входному файлу, имя выходного файла и путь к выходному файлу (путь может содержать только название директории, в таком случае название файла создается и подставляется в выходной путь автоматически), и направление перевода (пара языков).
Все данные на входе проверяются на корректность (пути на существование, языки на наличие в списке поддерживаемых языков Яндекс.Переводчика). Поля, в которых нужно ввести путь к выходному файлу и его имя, можно оставить пустыми, в данном случае переведенный файл будет сохранен в текущую рабочую директорию с автоматически созданным именем.
