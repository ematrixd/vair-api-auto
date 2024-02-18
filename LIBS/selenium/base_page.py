from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def main_page(self, main_url):
        return self.driver.get(main_url)

    def refresh_page(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    def wait_element(self, locator, time=170):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_item_disappears(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.find_element(locator)))

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def action_chains_click(self):
        """
        Метод создает экземпляр ActionChain для дальнейшего использования
        """
        return ActionChains(self.driver)
