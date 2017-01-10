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

