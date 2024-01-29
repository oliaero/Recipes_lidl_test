from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from tests.feature.page_object.recipes_page import RecipesPage


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.wait_until_loaded()

    def wait_until_loaded(self):
        self.driver.get("https://recetas.lidl.es/")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//li/a[@href="/todasrecetas"]')))  #'(//*[@href="/todasrecetas"])[1]')

    def accept_cookie_banner(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except TimeoutException:
                print("Cookie banner did not appear. Continue")

    def click_all_recipes_button(self):
        self.driver.find_element(By.XPATH,'//li/a[@href="/todasrecetas"]').click()
        return RecipesPage(self.driver, self.wait)

