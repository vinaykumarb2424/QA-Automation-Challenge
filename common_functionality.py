import os
import sys
from pathlib import Path
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()

    def get_element_by_id(self, id_, timeout=30):
        """
        this method takes id as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.ID, id_))
        )
        return element

    def get_element_by_name(self, name, timeout=30):
        """
        this method takes name as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.NAME, name))
        )
        return element

    def get_element_by_xpath(self, xpath, timeout=30):
        """
        this method takes xpath as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element

    def get_elements_by_xpath(self, xpath, timeout=30):
        """
        this method takes xpath as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        return element

    def get_presence_of_element_by_xpath(self, xpath, timeout=30):
        """
        this method takes xpath as parameter and return web element
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element

    def select_from_dropdown_using_text(self, locator, text, timeout=30):
        """
        this method will select the text in dropdown asper user text
        :param locator:
        :param text:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
        select = Select(element)
        select.select_by_visible_text(text)

    def switch_to_window(self, window_number, timeout=30):
        """
        this method will used to switch tabs
        :param window_number:
        :param timeout:
        :return:
        """
        window = self.driver.window_handles[int(window_number)]
        self.driver.switch_to.window(window)

    def page_refresh(self):
        """
        this method will refresh the page
        :return:
        """
        self.driver.refresh()

    def get_page_title(self):
        """
        return title of page focused
        :return:
        """
        return self.driver.title



