from zipfile import ZipFile

answer = set()

with ZipFile('main.zip', 'r') as zipObj:
    info = zipObj.namelist()
    print(info)
    for i in info:
        if i.endswith('.py'):
            answer.add(i[:i.rfind('/')])

with open('answer.txt', 'w') as outfile:
    for i in sorted(answer):
        outfile.write(i + '\n')