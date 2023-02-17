"""
    functions selenium web driver
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class SelDriver:
    """
        Selenium handler
    """
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    """
    def get_roulette_title(self):
        self.driver.get("https://wikiroulette.co/")
        title_element = self.driver.find_element(By.CSS_SELECTOR, "#firstHeading span")
        title = title_element.text
        print(title)
        return title
    """

    def get_website_title(self, website):
        try:
            self.driver.get(website)
            page_title = self.driver.title
            print(page_title)
            return (page_title)
        except:
            print('se site n\'existe pas !')
            return ''
