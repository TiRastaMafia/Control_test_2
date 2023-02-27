from Model.Note import Note
from Printer import Printer


class Save():

    # def __init__(self, file, file_count):
    #     self.file = file
    #     self.file_count = file_count


    def save_parameters(file, file_count, list_notes: Note, count: str):

            with open(file, 'r', encoding='utf-8'), open(file, 'w', encoding='utf-8') as f:
                for i in range(len(list_notes)):
                    f.write(f'{list_notes[i].id};{list_notes[i].title};{list_notes[i].message};{list_notes[i].date_time}')
                    f.writelines('\n')

            with open(file_count, 'r', encoding='utf-8'), open(file_count, 'w', encoding='utf-8') as k:
                k.write(str(count))

