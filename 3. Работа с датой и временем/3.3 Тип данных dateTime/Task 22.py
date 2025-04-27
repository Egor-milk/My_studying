from datetime import datetime

with open('D:/programm/PythonProjects/autotest/diary.txt', 'rt', encoding='utf-8') as file:
    a = file.read().split('\n')
    a.append('')
    note = {}
    temp = []
    for i in a:
        if i != '':
            temp.append(i)
        else:
            note[datetime.strptime(temp[0], '%d.%m.%Y; %H:%M')] = temp[1:]
            temp = []
    note = dict(sorted(note.items()))
    for key, value in note.items():
        print(datetime.strftime(key, '%d.%m.%Y; %H:%M'))
        print(*value, sep='\n')
        print()