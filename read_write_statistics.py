import csv

__author__ = 'Grzegorz'


def export_statistics(data, name='default_statistics_name.csv'):
    with open(name, 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=';')
        for key in sorted(data.keys()):
            data_writer.writerow([key, data[key]])      # s.encode('utf-8')
    print "***Data exported to file ", name

def import_statistics(data, name='default_statistics_name.csv'):
    with open(name, 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=';')
        for row in data_reader:
            data[row[0]] = float(row[1])
    print "Imported statistics for ", len(data), " days from ", name, " file"