def unique(a):
    b = []
    for i in range(len(a)):
        # Приводим каждый лист к стандартному виду
        # чтобы [a, b] == [b, a]
        c = sorted(a[i])
        # Если еще нет такого элемента - добавляем
        if c not in b:
            b.append(c)
    return b


def read_csv(_file_path):
    file = open(_file_path, encoding="utf-8")
    _tags = file.readline()
    _tags = list(_tags.split(','))
    # Костыль на первый столбец (ибо он изначально "undefined")
    _tags[0] = '\"id\"'
    # Костыль на последний столбец, ибо у него в конце "\n"
    _tags[len(_tags)-1] = _tags[len(_tags)-1][:-1]
    # Костыль на удаление лишних ебучих кавычек ибо они меня бесят
    for t in range(len(_tags)):
        _tags[t] = _tags[t][1:-1]

    # Двумерный массив строк csv файла
    _arr = []
    for line in file.readlines()[:10]:
        # Делим строку на столбцы
        _line = line.split(',')
        # Убираем "\n" из конца строки
        _line[len(_line)-1] = _line[len(_line)-1][:-1]
        # Убираем ебучие кавычки
        for l in range(len(_line)):
            _line[l] = _line[l][1:-1]
        _arr.append(_line)
    return _tags, _arr


def get_check(_tags, _data):
    _un = unique()