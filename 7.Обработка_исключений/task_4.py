file = input()

try:
    with open(file) as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')
