from Model.Note import Note

class Printer():

    def print_note(obj):
        try:
            print(
                f'id={obj.id}, datatime={obj.date_time}\ntitle={obj.title}\nmessage={obj.message}\n')
        except AttributeError:
            print ('Заметка с таким именем не найдена!')

    def print_list_notes(list_notes):
        for obj in list_notes:
            print(f'id = {obj.id}  |  title = {obj.title}')


