import time

__author__ = 'Grzegorz'

import main


urls = []
main.import_urls_to_crawl(urls)

for url in urls:
    print url

print "\n\n"


# curr_time = time.strftime("%Y-%m-%d-%H-%M", time.gmtime())
# tt= ["sdfs", "dasfd", "retyryuetr"]
# main.export_urls_to_crawl(tt, "proba.csv", "backup-"+curr_time)

# tt= [("sdfs", "zzzz"), ("dasfd", "xxxx"), ("retyryuetr", "bbbb")]
# main.export_crawled_data(tt, "proba.csv")
# aa=[]
# main.import_crawled_data(aa, "proba.csv")
# for a in aa:
#     print a



