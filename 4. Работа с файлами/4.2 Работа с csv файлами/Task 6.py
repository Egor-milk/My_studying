from autotest import basedir
import csv

with open(basedir + '\\wifi.csv', 'rt', encoding='utf-8') as file:
    wifi_point = {}
    d_reader = csv.DictReader(file, delimiter=';')
    for row in d_reader:
        wifi_point[row['district']] = wifi_point.get(row['district'], 0) + int(row['number_of_access_points'])


for key, value in sorted(wifi_point.items(), key=lambda item: (-int(item[1]), item[0])):
    print(f'{key}: {value}')