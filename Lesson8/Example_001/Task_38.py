
import csv


def look(phone_book):
    for elem in phone_book:
        print(' | '.join([f"{key}: {elem[key]}" for key in elem]))


def search(phone_book):
    request = input("Введите критерии поиска - ")
    results = []
    for elem in phone_book:
        if elem["имя"] == request:
            results.append(elem)
        else:
            if elem["фамилия"] == request:
                results.append(elem)
    else:
        if elem["номер"] == request:
            results.append(elem)
        else:
            if elem["описание"] == request:
                results.append(elem)
    return results                       

def add_member(phone_book):
    record = dict()
    for k in phone_book[0].keys():
        record[k] = input(f"Введите {k}: ")
        phone_book.append(record)

def write_csv(filename, phone_book):
    with open(filename, "a",oding = "utf - 8") as data:
        line = " "
        for v in phone_book[-1].values():
            line += v + ","
            data.write(f"{line[: -1]}\n")

def delete_member(phone_book):
    member = input("Введите парметры абонента: ")
    for elem in phone_book:
        for v in elem.values():
            if v == member:
                phone_book.remove(elem)

def rewrite_csv(filename, phone_book):
    with open(filename, "w", encoding = "utf - 8") as data:
        for i in range(len(phone_book)):
            line = " "
            for v in phone_book[i].values():
                line += v + ","
            data.write(f"{line[: -1]}\n")                

def change_data(phone_book):
    member = input("Введите имя или фамилию абонента: ")
    change = input("Введите критерий для изменения(имя, фамилия, номер, описание): ")
    new_value = input("Задайте новое значение: ")
    for elem in phone_book:
        for v in elem.values():
            if v == member:
                elem[change] = elem[change].replace(elem[change], new_value)


def show_menu():
    print("\n Выберите действие: \n"
          "1. Показать весь справочник\n"
          "2. Поиск по справочнику\n"
          "3. Добавить новую запись\n"
          "4. Удалить запись контакта\n"
          "5. Изменить данные контакта\n"
          "6. Завершение работы")
    command = int(input("Команда: "))
    return command


def parse_csv(filename):
    results = []
    listfields = ["имя", "фамилия", "номер", "описание"]
    with open(filename, "r", encoding="utf - 8") as data:
        for line in data:
            record = dict(zip(listfields, line.strip().split(",")))
            results.append(record)
    return results

def use_phone_book():
    command = show_menu()
    phone_book = parse_csv("Lesson8/Example_001/Phone_book.csv")

    while (command != 7):
        if command == 1:
            look(phone_book)
        elif command == 2:
            search(phone_book)
        elif command == 3:
            add_member(phone_book)
            write_csv("Phone_book.csv", phone_book)
        elif command == 4:
            delete_member(phone_book)
            rewrite_csv("Phone_book.csv", phone_book)
        elif command == 5:
            change_data(phone_book)
            rewrite_csv("Phone_book.csv", phone_book)
        elif command == 6:
            print("Работа завершена")
            raise SystemExit
        command = show_menu()

use_phone_book()
