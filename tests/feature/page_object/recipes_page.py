from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import time


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

    def wait_until_dropdown_menu_is_loaded(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//*[@class="nuc-a-flex-item nuc-a-flex-item--width-12 nuc-a-flex-item--show-overflow"])[3]')))


    def click_desserts_button(self):
        self.driver.find_element(By.XPATH, '(//*[@class="nuc-a-flex-item nuc-a-flex-item--width-12 nuc-a-flex-item--show-overflow"])[3]').click()

    def get_number_desserts_recipes_from_dropdown_menu(self):
        return self.driver.find_element(
            By.XPATH, '//*[@name="f63ec0ec-82e8-4205-a0d1-cd24c5176197"]/following-sibling::span[@class="nuc-m-checkbox__label-count"]').text


    def get_total_result_number_recipes(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.lirc-o-recipe-search__total-results-text').text

    def click_load_more_button(self):

        s = self.driver.find_element(By.CSS_SELECTOR, '.lirc-o-recipe-search__load-more-button')
        self.driver.execute_script("arguments[0].click();", s)

    def wait_until_more_recipes_loaded(self):
        self.driver.wait.until(EC.
        self.count_items_on_the_page() > 36)

    def count_items_on_the_page(self):
        list_of_items = self.driver.find_elements(By.CSS_SELECTOR,
                                 '[class="nuc-a-flex-item nuc-a-flex-item--width-12 nuc-a-flex-item--width-6@sm nuc-a-flex-item--width-4@md nuc-a-flex-item--show-overflow"]')
        count = 0
        for item in list_of_items:
            count += 1
        total_count = count
        return total_count

    def click_collection_button(self):
        self.driver.find_element(By.XPATH, '//button/span[text()="Ocasiones especiales"]').click()

    def click_valentin_day_button(self):
        self.driver.find_element(By.XPATH, '//*[@name="05cbddce-fa68-4d5d-ad1e-4f0828f85de3"]/following-sibling::label[@class="nuc-m-checkbox__label"]').click()

    def click_remove_valentin_day_filter(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-filter-id="05cbddce-fa68-4d5d-ad1e-4f0828f85de3"]')

    def click_sorted_by_dropdown(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="lirc-o-recipe-search__order-select-field lirc-m-select-field__select nuc-a-select"]').click()

    def click_total_time_sorted(self):
        self.driver.find_element(By.CSS_SELECTOR, '[value="total_time"]').click()

    def get_cooking_time_first_recipe(self):
        [id = "result-page-1"]
    def get_cooking_time_last_recipe(self):
        (// *[@class ="lirc-o-card lidl-o-card nuc-o-card"])[36]