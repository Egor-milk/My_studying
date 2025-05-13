import csv

from autotest import basedir

def condense_csv(file, id_name='ID'):
    with open(basedir + '\\' +file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        dict_property = {}
        for line in reader:
            dict_property.setdefault(line[0], {})
            dict_property[line[0]].setdefault(line[1], line[2])
    #return dict_property

    with open(basedir + '\\' + 'condensed.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        line_to_write = [id_name] + list(dict_property[list(dict_property.keys())[0]].keys())
        writer.writerow(line_to_write)
        for i in dict_property:
            line_to_write = [i] + list(dict_property[i].values())
            writer.writerow(line_to_write)

condense_csv('4')