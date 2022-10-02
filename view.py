def menu() -> int:
    print('\nЧто делаем:\n'
          '1. Посмотреть список сотрудников\n'
          '2. Поиск по фамилии\n'
          '3. Поиск по должности\n'
          '4. Добавить сотрудника\n')
    choice = int(input())
    return choice

def directory_show(data):
    for l in data:
        x = ''
        for v, k, in l.items():
            x += f'{v}:{k}\n'
        print(x)


def directory_find_name() -> str:
    return input('Фамилия для поиска: ')


def directory_find_position() -> str:
    return input('Должность для поиска: ')


def directory_write() -> str:
    l_name = input('Фамилия: ')
    f_name = input('Имя: ')    
    position = input('Должность: ')
    salary = input('Оклад: ')
    premium = input('Размер премии: ')
    
    return f'{l_name}, {f_name}, {position}, {salary}, {premium} '