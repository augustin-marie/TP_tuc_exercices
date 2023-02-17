from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

#def get_roulette_title():
#    driver.get("https://wikiroulette.co/")
#    title_element = driver.find_element(By.CSS_SELECTOR, "#firstHeading span")
#    title = title_element.text
#    print(title)
#    return title

def get_website_title(website):
    try:
        driver.get(website)
        page_title = driver.title
        print(page_title)
        return page_title
    except:
        print('se site n\'existe pas !')
        return ''

if __name__ == '__main__':
    driver.get_website_title("https://www.reddit.com/")