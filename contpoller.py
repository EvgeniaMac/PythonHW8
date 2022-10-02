from view import (menu, directory_show, directory_find_name,
                  directory_find_position, directory_write)
from mod import (write_csv, write_txt, read_scv, add_user,
                 find_name, find_position)


def work_employees():
    ch = menu()
    em_book = read_scv('Employees.csv')
    while ch != 4:
        if ch == 1:
            directory_show(em_book)
        elif ch == 2:
            name = directory_find_name()
            print(find_name(em_book, name))
        elif ch == 3:
            num = directory_find_position()
            print(find_position(em_book, num))
        elif ch == 4:
            user_data = directory_write()
            add_user(em_book, user_data)
            write_csv('Employees.csv', em_book)
        ch = menu()
