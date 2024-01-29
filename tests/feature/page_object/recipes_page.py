from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class RecipesPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.wait_until_loaded()

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//button/span[text()="Tipo de plato"]')))

    def get_hot_dog_recipe(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(),"Hot dog")]')

    def click_course_button(self):
        self.driver.find_element(By.XPATH, '//button/span[text()="Tipo de plato"]').click()

    def click_desserts_button(self):
        self.driver.find_element(By.ID, 'nuc-1311387066"').click()

    def get_number_desserts_recipes_from_dropdown_menu(self):
        return self.driver.find_element(
            By.XPATH, '//*[@id="nuc-1311387066"]/following-sibling::*[@class="nuc-m-checkbox__label-count"]').text

    def get_total_result_number_recipes(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.lirc-o-recipe-search__total-results-text').text
