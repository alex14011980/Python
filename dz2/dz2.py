'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

д.з Дополнить справочник возможностью копирования данных из одного
файла в другой. Пользователь вводит номер строки,
которую необходимо перенести из одного файла в другой.
'''

from os.path import exists
from csv import DictReader, DictWriter





class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите имя: ")
            if len(last_name) < 2:
                raise NameError("Не валидное имя")
            else:
                is_valid_last_name = True
        except NameError as err:
            print(err)
            continue


    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue


        return [first_name, last_name, phone_number]


def create_file(file_name):
    # with - Менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)



def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже есть")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)



def copy_write(file_name, new_file_name):
    with open(file_name, "r", encoding='utf-8') as data: #Открываем существующий файл
        f_reader = DictReader(data)
        reader = list(f_reader)
        #Проверяем ввод на длину списка
        is_valid_num = False
        while not is_valid_num:
            try:
                num = int(input("Введите номер строки:  "))
                if num not in range(len(reader)):
                   raise LenNumberError("Такой строки нет!")
                else:
                    is_valid_num = True
            except ValueError:
                print("Не валидный номер!!!")
                continue
            except LenNumberError as err:
                print(err)
                continue
        #Создаем пустой список
        res = list()
        res.append(reader[num])     #Добавляем в него нужную строку


    with open(new_file_name, "w", encoding='utf-8', newline='') as data:    #Открываем вновь созданный или уже имеющийся файл
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)         #Записываем в файл созданный список


new_file_name = 'phone_1.csv'
file_name = 'phone.csv'



def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
            if not exists(new_file_name):
                create_file(new_file_name)
                write_file(new_file_name)
            print(copy_write(file_name, new_file_name))

main()