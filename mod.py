def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            x = ' '
            for v in data[i].values():
                x += v+','
            fout.write(f'{x[:-1]}\n')


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            x = ' '
            for v in data[i].values():
                x += v+','
            fout.write(f'{x[:-1]}\n')


def read_scv(filname: str) -> str:
    data = []
    fields = ['Фамилия', 'Имя', 'Должность', 'Оклад', 'Размер премии']
    with open(filname, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
        return data


def find_name(data: list, l_name: str) -> str:
    for l in data:
        if l.get('Фамилия') == l_name:
            return f'{l.get("Должность")} {l.get("Оклад")} {l.get("Размер премии")}'
        
        return 'Нет такого сотрудника'


def find_position(data: list, position: str) -> str:
    for l in data:
        if l.get('Должность') == position:
            return f'{l.get("Фамилия")} {l.get("Имя")} {l.get("Оклад")} {l.get("Размер премии")}'
        return 'Нет такой должности'


def add_user(data: list, user_data: str):
    fietds = ['Фамилия', 'Имя', 'Должность', 'Оклад', 'Размер премии']
    record = dict(zip(fietds, user_data.split(',')))
    data.append(record)
