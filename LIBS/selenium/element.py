from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from LIBS.base_page import BasePage

class LocatorValue():

    @staticmethod
    def by_xpath(xpath_value):
        return (By.XPATH, '{}'.format(xpath_value))

    @staticmethod
    def by_name(text_value):
        return (By.NAME, '{}'.format(text_value))

    @staticmethod
    def by_link_text(text_value):
        return (By.LINK_TEXT, '{}'.format(text_value))

    @staticmethod
    def by_css(text_value):
        return (By.CLASS_NAME, '{}'.format(text_value))


class ElementTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_xpath_button(self, xpath: str):
        self.wait_element(LocatorValue.by_xpath(xpath))
        self.find_element(LocatorValue.by_xpath(xpath)).click()

    def click_clamped_control(self, xpath: list):
        AC = self.action_chains_click()
        AC.key_down(Keys.CONTROL).perform()
        for idx in range(len(xpath)):
            self.find_element(LocatorValue.by_xpath(xpath[idx])).click()
        AC.key_up(Keys.CONTROL).perform()

    def clear_input(self, xpath):
        self.find_element(LocatorValue.by_xpath(xpath)).clear()

    def get_text_for_element(self, xpath, all_elem=False):
        if all_elem:
            return [x.text for x in self.find_elements(LocatorValue.by_xpath(xpath))]
        else:
            return self.find_element(LocatorValue.by_xpath(xpath)).text

    def get_class_for_element(self, xpath):
        return self.find_element(LocatorValue.by_xpath(xpath)).get_attribute("class")

    def fill_input(self, xpath, value):
        self.clear_input(xpath)
        self.find_element(LocatorValue.by_xpath(xpath)).send_keys(value)

    def wait_item(self, xpath, time=170):
        self.wait_element(LocatorValue.by_xpath(xpath), time=time)

    def wait_item_invisibility(self, xpath):
        self.wait_item_disappears(LocatorValue.by_xpath(xpath))

    def assert_value_text(self, xpath, value):
        assert self.find_element(LocatorValue.by_xpath(xpath)).text == value

    def insert_file(self, xpath, path_file):
        button = self.find_element(LocatorValue.by_xpath(xpath))
        button.send_keys(path_file)

    def check_exists_by_xpath(self, xpath):
        try:
            from time import sleep
            sleep(1)
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
