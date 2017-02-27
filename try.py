from selenium.common.exceptions import NoSuchElementException

__author__ = 'Grzegorz'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.implicitly_wait(15)



driver.get('http://www.politico.com/blogs/2016-dem-primary-live-updates-and-results/2016/04/bernie-sanders-john-kasich-221456')
elem = driver.find_element_by_xpath("//time")
print elem.get_attribute('datetime')[0:10]

# try:
driver.find_element_by_xpath('//*[@id="showCommentsButton"]').click()
#
driver.implicitly_wait(20)
print "sprobuje rozwijac liste"
print len(driver.find_elements_by_xpath('/button'))
while len(driver.find_elements_by_css_selector('._1gl3._4jy0._4jy3._517h._51sy._42ft')) > 0:
    print "proba "
    # driver.find_elements_by_class_name("_1gl3")[0].click()
    driver.find_elements_by_class_name("_1gl3 _4jy0 _4jy3 _517h _51sy _42ft")[0].click()


driver.switch_to.default_content()
fff = driver.find_element_by_class_name('fb_ltr')       # Facebook Social Plugin
print fff.get_attribute("title"), fff.get_attribute("id"), fff.get_attribute("name")

driver.switch_to.frame(fff.get_attribute("name"))
print driver.title

driver.implicitly_wait(10)
print "sprobuje rozwijac liste"
# print len(driver.find_elements_by_xpath('/button'))
print len(driver.find_elements_by_css_selector('#u_0_0 > div > div > div._4k-6 > div._5o4h > button'))
while len(driver.find_elements_by_css_selector('#u_0_0 > div > div > div._4k-6 > div._5o4h > button')) > 0:
    print "proba "
    # driver.find_elements_by_class_name("_1gl3")[0].click()
    driver.find_elements_by_class_name("_1gl3 _4jy0 _4jy3 _517h _51sy _42ft")[0].click()



# for e in driver.find_elements_by_class_name("_5mdd"):
#     print e, e.text

# except :
#     print "should i try again? damn, no!"

# elems = driver.find_elements_by_xpath('/span[class="_5mdd"]/span')

# elems = driver.find_elements_by_xpath('//*[@id="u_0_0"]/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div[1]/div/span/span/span')
# for e in elems:
#     print e.text


# driver.get('http://www.politico.com/search?adv=true&start=04/01/2016&end=11/16/2016&pv=00000150-1a34-d6c0-a9fb-bfb4f0a50000&s=oldest')
#
# print "title: " + driver.title
# elems = driver.find_elements_by_xpath("//article[@class='story-frag format-ml']/div/header/h3/a")
# for e in elems:
#     print e.get_attribute('href')
#
# print "find next page"
# try:
#     next_search = driver.find_element_by_xpath(u'//nav/div/a[contains(text(),"Next page!!!!!!!!")]')
#     print next_search.get_attribute('href')
# except NoSuchElementException:
#     print "niemateakiegobicia"


##########################################################################################
##########################################################################################
#### analyser - tries

# import nltk
#
# class Splitter(object):
#     def __init__(self):
#         self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
#         self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()
#
#     def split(self, text):
#         """
#         input format: a paragraph of text
#         output format: a list of lists of words.
#             e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
#         """
#         sentences = self.nltk_splitter.tokenize(text)
#         tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
#         return tokenized_sentences
#
#
# class POSTagger(object):
#     def __init__(self):
#         pass
#
#     def pos_tag(self, sentences):
#         """
#         input format: list of lists of words
#             e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
#         output format: list of lists of tagged tokens. Each tagged tokens has a
#         form, a lemma, and a list of tags
#             e.g: [[('this', 'this', ['DT']), ('is', 'be', ['VB']), ('a', 'a', ['DT']), ('sentence', 'sentence', ['NN'])],
#                     [('this', 'this', ['DT']), ('is', 'be', ['VB']), ('another', 'another', ['DT']), ('one', 'one', ['CARD'])]]
#         """
#
#         pos = [nltk.pos_tag(sentence) for sentence in sentences]
#         #adapt format
#         pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
#         return pos
#
#
# # crawled_data = []
# # rwlib.import_crawled_data(crawled_data)
# comment1 = 'Once again the Trump organization shows they don\'t do their homework, understand the process, or hire the right people. "Make America Unprepared".'
#
# text = """What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid."""
#
# splitter = Splitter()
# postagger = POSTagger()
#
# splitted_sentences = splitter.split(text)
# print splitted_sentences
# pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
# print pos_tagged_sentences