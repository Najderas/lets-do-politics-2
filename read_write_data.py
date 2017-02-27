__author__ = 'Grzegorz'

import os
import unicodecsv as csv


def import_crawled_data(data, name=None):
    with open((name or "data_crawled_data.csv"), 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=chr(9), quotechar='|')
        for row in data_reader:
            # print row[0], "  --  ", row[1]
            # data.append((row[0].decode('utf-8'), row[1].decode('utf-8')))
            data.append((row[0], row[1]))
    print "Imported ", len(data), " comments"


def import_crawled_urls(urls, name=None):
    with open((name or "data_crawled_urls.csv"), 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=chr(9), quotechar='|')
        for row in data_reader:
            # print row[0].decode('utf-8')
            urls.append(row[0].decode('utf-8'))
    print "Imported ", len(urls), " crawled urls"


def import_urls_to_crawl(urls, name=None):
    with open((name or "data_urls_to_crawl.csv"), 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=chr(9), quotechar='|')
        for row in data_reader:
            urls.append(row[0].decode('utf-8'))
    print "Imported ", len(urls), " urls to crawl"


def export_crawled_data(data, name=None, folder=None):
    with open((name or 'data_crawled_data.csv'), 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            # data_writer.writerow([row[0].encode('utf-8'), row[1].encode('utf-8')])      # s.encode('utf-8')
            data_writer.writerow([row[0], row[1]])      # s.encode('utf-8')
        print "***Data exported to file ", (name or 'data_crawled_data.csv')

    if folder:
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder + '/' + (name or 'data_crawled_data.csv'), 'wb') as csvfile:
            data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                data_writer.writerow([s.encode('utf-8') for s in row])
            print "***Data exported to backup file ", folder + "/" + (name or 'data_crawled_data.csv')


def export_crawled_urls(urls, name=None, folder=None):
    with open((name or 'data_crawled_urls.csv'), 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for url in urls:
            data_writer.writerow([url.encode('utf-8'), ])
        print "***List of crawled URLs exported to file ", (name or "data_crawled_urls.csv")

    if folder:
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder + '/' + (name or 'data_crawled_urls.csv'), 'wb') as csvfile:
            data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for url in urls:
                data_writer.writerow([url.encode('utf-8'), ])
            print "***List of crawled URLs exported to backup file ", folder + '/' + (name or "data_crawled_urls.csv")


def export_urls_to_crawl(urls, name=None, folder=None):
    with open((name or 'data_urls_to_crawl.csv'), 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for url in urls:
            data_writer.writerow([url.encode('utf-8'), ])
        print "***List of URLs to crawl exported to file ", (name or "data_urls_to_crawl.csv")
    if folder:
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder + '/' + (name or 'data_urls_to_crawl.csv'), 'wb') as csvfile:
            data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for url in urls:
                data_writer.writerow([url.encode('utf-8'), ])
            print "***List of URLs to crawl exported to backup file ", folder + '/' + (name or "data_urls_to_crawl.csv")


