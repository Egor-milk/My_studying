with open('D:/programm/PythonProjects/autotest/diary.txt', 'rt', encoding='utf-8') as file:
    a = file.read().split('\n\n')
    print(*a)