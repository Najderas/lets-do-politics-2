import os
import crawler as Crawler
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def import_crawled_data(data, name=None):
    with open((name or "data_crawled_data.csv"), 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=chr(9), quotechar='|')
        for row in data_reader:
            data.append((row[0].decode('utf-8'), row[1].decode('utf-8')))


def import_crawled_urls(urls, name=None):
    with open((name or "data_crawled_urls.csv"), 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=chr(9), quotechar='|')
        for row in data_reader:
            print row[0].decode('utf-8')
            urls.append(row[0].decode('utf-8'))


def import_urls_to_crawl(urls, name=None):
    with open((name or "data_urls_to_crawl.csv"), 'rb') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=chr(9), quotechar='|')
        for row in data_reader:
            urls.append(row[0].decode('utf-8'))


def export_crawled_data(data, name=None, folder=None):
    with open((name or 'data_crawled_data.csv'), 'wb') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=chr(9), quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            data_writer.writerow([s.encode('utf-8') for s in row])
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

# os.environ["webdriver.chrome.driver"] = chromedriver

if __name__ == "__main__":
    crawled_data = []
    crawled_urls = []
    urls_to_crawl = [
        'http://www.politico.com/search?adv=true&start=04/01/2016&end=11/16/2016&pv=00000150-1a34-d6c0-a9fb-bfb4f0a50000&s=oldest']

    import_crawled_data(crawled_data)
    import_crawled_urls(crawled_urls)
    import_urls_to_crawl(urls_to_crawl)

    new_crawled_data = []


    print "\ncrawled data"
    for d in crawled_data:
        print d

    print "\nurls to crawl"
    print "---".join(urls_to_crawl)

    print "\ncrawled urls"
    print "---".join(crawled_urls)





    # crawler = Crawler.WebCrawler(urls_to_crawl, crawled_urls, new_crawled_data)
    #
    # try:
    #     crawler.start(300)
    # except:
    #     pass
    #
    # print "Summary: ", len(new_crawled_data), " new comments"
    #
    # crawled_data.extend(new_crawled_data)
    #
    # curr_time = time.strftime("%Y-%m-%d-%H-%M", time.gmtime())
    # export_crawled_data(crawled_data, None, "backup-"+curr_time)
    # export_crawled_urls(crawled_urls, None, "backup-"+curr_time)
    # export_urls_to_crawl(urls_to_crawl, None, "backup-"+curr_time)






    # chromedriver = "chromedriver.exe"
    # chromeOptions = webdriver.ChromeOptions()
    # prefs = {"profile.managed_default_content_settings.images":2}
    # chromeOptions.add_experimental_option("prefs",prefs)
    # driver = webdriver.Chrome(chrome_options=chromeOptions)
    # # driver = webdriver.Chrome(chromedriver)
    # # driver = webdriver.Chrome()
    #
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()
