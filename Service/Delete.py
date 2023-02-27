
from Model.Note import Note

class Delete:

    def dell_note(list_notes: Note):
        title_for_del = input('Введите заголовок для удаления: \n')
        for obj in list_notes:
            if (obj.title.lower() == title_for_del.lower()):
                list_notes.remove(obj)
                print('Заметка успешно удалена!')

