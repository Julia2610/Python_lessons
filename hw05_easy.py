# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def new_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print("Директория успешно создана")
    except FileExistsError:
        print("Такая директория уже существует")
    except PermissionError:
        print("Недостаточно прав для создания директории")

# dir_name = []
# for i in range(1, 10):
#     dir_name = "dir_" + str(i)
# print(new_dir(dir_name))

def del_dir(dir_name):
    try:
        os.rmdir(dir_name)
        print("Директория удалена")
    except FileExistsError:
        print("Такой директории не существует")
    except PermissionError:
        print("Недостаточно прав для удаления директории")

# dir_name = []
# for i in range(1, 10):
#     dir_name = "dir_" + str(i)
#     print(del_dir())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    list = os.listdir(path='.')
    print('Список файлов в текущей директории:')
    for element in list:
        print(element)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(current_file_copy())


