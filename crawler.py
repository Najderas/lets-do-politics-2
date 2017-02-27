from selenium.common.exceptions import NoSuchElementException

__author__ = 'Grzegorz'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# from src.models import ArticleOrComment, Author


class WebCrawler(object):
    def __init__(self, urls_to_crawl, crawled_urls, new_crawled_data):
        """
        creates a new web crawler object with given url and a set of parent web crawlers urls in order to prevent loops.
        :param url: String
        :param existing_crawlers_urls: set(String)
        :return:
        """
        self.urls_to_crawl = urls_to_crawl
        self.crawled_urls = crawled_urls
        self.results = new_crawled_data

    def find_urls(self, driver):
        """
        :param input_string: String
        :return: List[String]
        """
        # TODO  remember not to leave domain
        urls = []
        articles = driver.find_elements_by_xpath("//article[@class='story-frag format-ml']/div/header/h3/a")
        for e in articles:
            url = e.get_attribute('href')
            urls.append(url)
            print "found link: ", url

        try:
            next_search = driver.find_element_by_xpath(u'//nav/div/a[contains(text(),"Next page")]')
            next_search_url = next_search.get_attribute('href')
            urls.append(next_search_url)
            print "found link: ", next_search_url
        except NoSuchElementException:
            print "Next search page not found"

        return urls
# //article[@class='story-frag format-ml']/div/header/h3/a

    def parse_comments(self, driver, date):
        # driver.find_element_by_id('showCommentsButton').click()
        # fb = driver.find_element_by_xpath('//iframe[@title="Facebook Social Plugin"')
        # print fb
        comments = []

        try:
            driver.find_element_by_xpath('//*[@id="showCommentsButton"]').click()

            driver.switch_to.default_content()
            fff = driver.find_element_by_class_name('fb_ltr')       # Facebook Social Plugin
            # print fff.get_attribute("title"), fff.get_attribute("id"), fff.get_attribute("name")

            driver.switch_to.frame(fff.get_attribute("name"))
            print driver.title

            # for e in driver.find_elements_by_xpath('/span[@class="_5mdd"]/span'):
            for e in driver.find_elements_by_class_name("_5mdd"):
                # print e, e.text
                comments.append((date, e.text.replace('\n', '   ').replace('\r', '')))
        except:
            print "should i try again? damn you!"
        finally:
            driver.switch_to.default_content()

        return comments

    def crawl(self, driver):
        """
        crawls the given url, and returns a list of all possible objects to be created.
        """
        comments = []

        # get current url
        if len(self.urls_to_crawl) > 0:
            current_url = self.urls_to_crawl.pop(0)
        else:
            print "Nothing more to crawl"
            return ()

        if current_url in self.crawled_urls:
            print "Entered url already crawled"
            return ()

        print "Visiting ", current_url

        # load page with driver
        driver.get(current_url)
        # element = driver.find_element_by_id("showCommentsButton")

        if ("POLITICO Site Search - POLITICO" in driver.title):     # this is search page
            # find new urls
            url_list = self.find_urls(driver)
            for url in url_list:
                if not url in self.crawled_urls:
                    self.urls_to_crawl.append(url)
        else:                       # this is article page
            date = driver.find_element_by_xpath("//time").get_attribute('datetime')[0:10]

            comments = self.parse_comments(driver, date)
            print "Article date: ", date, " Found ", len(comments), " comments"

        self.crawled_urls.append(current_url)

        return comments

    def start(self, number_to_crawl=10):

        # chromedriver = "chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chromeOptions)
        driver.implicitly_wait(10)

        for i in xrange(int(number_to_crawl)):
            print "##### ", i, " #####"
            self.results.extend(self.crawl(driver))

            if (i+1) % 50 == 0:
                driver.close()
                driver = webdriver.Chrome(chrome_options=chromeOptions)
                driver.implicitly_wait(10)

        driver.close()


