import os
import crawler as Crawler
import read_write_data as rwlib
import sentiment_analyser as analyser
import read_write_statistics as rwstats
import time
import winsound
import matplotlib.pyplot as plt

sites_to_crawl = 100

# os.environ["webdriver.chrome.driver"] = chromedriver

def main_crawl():
    global sites_to_crawl
    crawled_data = []
    crawled_urls = []
    urls_to_crawl = [
        # 'http://www.politico.com/search?adv=true&start=04/01/2016&end=11/16/2016&pv=00000150-1a34-d6c0-a9fb-bfb4f0a50000&s=oldest'
        # 'http://www.politico.com/blogs/2016-presidential-debate-fact-check/2016/10/trump-cant-get-it-right-on-clintons-email-deletion-229469',
        # 'http://www.politico.com/blogs/2016-presidential-debate-fact-check/2016/10/fact-trump-supported-the-war-in-iraq-before-he-opposed-it-229470',
        # 'http://www.politico.com/story/2016/10/2016-presidential-debate-donald-trump-muslim-ban-extreme-vetting-229468',
        # 'http://www.politico.com/blogs/2016-presidential-debate-fact-check/2016/10/trump-gets-clintons-tax-plan-totally-wrong-229479',
        # 'http://www.politico.com/search/252?s=oldest&adv=true&start=04%2F01%2F2016&end=11%2F16%2F2016&pv=00000150-1a34-d6c0-a9fb-bfb4f0a50000'
    ]

    rwlib.import_crawled_data(crawled_data)
    rwlib.import_crawled_urls(crawled_urls)
    rwlib.import_urls_to_crawl(urls_to_crawl)

    new_crawled_data = []

    print "\nurls to crawl:"
    for url in urls_to_crawl:
        print url

    crawler = Crawler.WebCrawler(urls_to_crawl, crawled_urls, new_crawled_data)

    retry = 10
    while retry > 0:
        try:
            crawler.start(sites_to_crawl)
            retry = 0
        except:
            print "#####################"
            print "##  ERROR OCCURED  ##"
            print "#####################"
            retry -= 1
            sites_to_crawl /= 1.6

    crawled_data.extend(new_crawled_data)

    print "Summary: found ", len(new_crawled_data), " new comments, of ", len(crawled_data), " all"

    curr_time = time.strftime("%Y-%m-%d-%H-%M", time.gmtime())
    rwlib.export_crawled_data(crawled_data, None, "backup-"+curr_time)
    rwlib.export_crawled_urls(crawled_urls, None, "backup-"+curr_time)
    rwlib.export_urls_to_crawl(urls_to_crawl, None, "backup-"+curr_time)

    winsound.Beep(440, 3000)   # frequency, duration


def main_analyze():

    crawled_data = []
    rwlib.import_crawled_data(crawled_data)

    (trump_summary, clinton_summary) = analyser.analyse_sentiment(crawled_data)

    rwstats.export_statistics(trump_summary, "data_sentiment_trump.csv")
    rwstats.export_statistics(clinton_summary, "data_sentiment_clinton.csv")


def create_chart():

    trump_summary = dict()
    rwstats.import_statistics(trump_summary, "data_sentiment_trump.csv")

    trump_summary_list = [(key, value) for key, value in trump_summary.items()]
    trump_summary_list.sort(key=lambda a: a[0])

    trump_x = [a[0] for a in trump_summary_list]
    trump_y = [a[1] for a in trump_summary_list]
    summmary_sent = 0
    trump_y_summarized = []
    for sen in trump_y:
        summmary_sent += sen
        trump_y_summarized.append(summmary_sent)
    # print " # ".join(map(lambda x: str(x), trump_y_summarized))

    clinton_summary = dict()
    rwstats.import_statistics(clinton_summary, "data_sentiment_clinton.csv")

    clinton_summary_list = [(key, value) for key, value in clinton_summary.items()]
    clinton_summary_list.sort(key=lambda a: a[0])

    clinton_x = [a[0] for a in clinton_summary_list]
    clinton_y = [a[1] for a in clinton_summary_list]
    summmary_sent = 0
    clinton_y_summarized = []
    for sen in clinton_y:
        summmary_sent += sen
        clinton_y_summarized.append(summmary_sent)

    step = 20

    x = range(len(trump_y_summarized))
    plt.plot(x, trump_y_summarized, 'r', label="Trump")
    # plt.plot(x, trump_y, 'r', label="Trump")
    plt.xticks(x[::step], trump_x[::step], rotation='vertical')
    plt.legend(loc="lower left", shadow=True, fancybox=True)

    x = range(len(clinton_y_summarized))
    plt.plot(x, clinton_y_summarized, 'b', label="Clinton")
    # plt.plot(x, clinton_y, 'b', label="Clinton")
    plt.xticks(x[::step], clinton_x[::step], rotation='vertical')
    plt.legend(loc="lower left", shadow=True, fancybox=True)

    plt.savefig("result_plot")
    # plt.savefig("result_plot_not_summarized")
    plt.show()

if __name__ == "__main__":

    # main_crawl()

    # main_analyze()

    create_chart()

