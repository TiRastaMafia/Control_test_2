import sys
sys.path.insert(0, 'Service')
from Add import Add
from Download import Download
from Delete import Delete
from Printer import Printer
from Edit import Edit
from Search import Search
from Save import Save

file = 'SystemDate\\save_notes.csv'
file_count = 'SystemDate\\save_count.txt'

class Controller():

    def button_click():

        # content_notes = 'SystemDate\\save_notes.csv'
        # count = 'SystemDate\\save_count.txt'
        add = Add
        download = Download
        printer = Printer
        edit = Edit
        delete = Delete
        search = Search
        # save = Save('SystemDate\\save_notes.csv', 'SystemDate\\save_count.txt')
        save = Save

        condition = True

        list_notes = download.import_data('SystemDate\\save_notes.csv')
        id = download.import_count('SystemDate\\save_count.txt')

        while (condition):
            # try:
                task = input("МЕНЮ: \n"
                                 "1 - Создать заметку \n"
                                 "2 - Удалить заметку \n"
                                 "3 - Изменить заметку \n"
                                 "4 - Показать заметки \n"
                                 "5 - Поиск  \n"
                                 "6 - Сохранение \n"
                                 "7 - Выход \n"
                                 "Введи нужную цифру: \n")
                if task == '1':
                    list_notes.append(add.add(id))
                    id += 1
                elif task == '2':
                    printer.print_list_notes(list_notes)
                    delete.dell_note(list_notes)
                elif task == '3':
                    inner_condition = True
                    while inner_condition:
                        inner_task = int(input('Что хотите изменить?\n'
                                               '1. Изменить заголовок\n'
                                               '2. Изменить содержание\n'
                                               '3. Отмена\n'
                                               'Введи нужную цифру: \n'))
                        if inner_task == 1:
                            edit.modify_title(edit.enter_note(list_notes))
                        elif inner_task == 2:
                            edit.modify_message(edit.enter_note(list_notes))
                        elif inner_task == 3:
                            inner_condition = False
                        else:
                            print('Введена неверная команда!\n')
                elif task == '4':
                    inner_condition = True
                    while inner_condition:
                        inner_task = int(input('Что хотите вывести?\n'
                                               '1. Все заметки\n'
                                               '2. Заметку (по заголовку)\n'
                                               '3. Отмена\n'
                                               'Введи нужную цифру: \n'))
                        if inner_task == 1:
                            printer.print_list_notes(list_notes)
                            break
                        elif inner_task == 2:
                            printer.print_note(edit.enter_note(list_notes))
                            break
                        elif inner_task == 3:
                            inner_condition = False
                        else:
                            print('Введена неверная команда!\n')
                elif task == '5':
                    printer.print_note(search.search_note(list_notes))
                elif task == '6':
                    save.save_parameters(file, file_count, list_notes, id)
                elif task == '7':
                    inner_condition = True
                    while inner_condition:
                        inner_task = int(input('Сохранить изменения перед выходом?\n'
                                               '1. Да\n'
                                               '2. Нет\n'
                                               '3. Отмена\n'
                                               'Введи нужную цифру: \n'))
                        if inner_task == 1:
                            save.save_parameters(file, file_count, list_notes, id)
                            condition = False
                            print("Программа завершена.")
                            break
                        elif inner_task == 2:
                            print("Программа завершена.")
                            condition = False
                            break
                        elif inner_task == 3:
                            inner_condition = False
                        else:
                            print('Введена неверная команда!\n')
            # except:
