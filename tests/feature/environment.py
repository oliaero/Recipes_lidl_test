from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def before_all(context):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome("/Users/olia/work/webdrivers/chromedriver", options=options)
    context.wait = WebDriverWait(context.driver, 5)


def after_all(context):
    context.driver.quit()