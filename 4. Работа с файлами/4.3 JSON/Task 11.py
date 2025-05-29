from autotest import basedir
import json, csv


with open(basedir + '\\students.json', 'r', encoding='utf-8') as file_to_read:
    students = json.load(file_to_read)

students = sorted(filter(lambda student: int(student['age']) >= 18 and int(student['progress']) >= 75, students), key=lambda student: student['name'])
with open(basedir + '\\data.csv', 'w', encoding='utf-8', newline='') as file_to_write:
    d_writer = csv.DictWriter(file_to_write, fieldnames=['name', 'phone'])
    d_writer.writeheader()
    for i in students:
        d_writer.writerow({'name': i['name'], 'phone': i['phone']})
