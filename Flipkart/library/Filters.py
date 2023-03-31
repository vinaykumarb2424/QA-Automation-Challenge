import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
from abcdefgh.common_functionality import *
from abcdefgh.Flipkart.map import filters as map
from selenium.webdriver.support.select import Select


class Filters:
    def __init__(self, driver):
        print("{}".format(self.__init__.__doc__))
        self.driver = driver
        print("webdriver created")

    def filter_products(self):
        try:
            verify_result = self.driver.get_presence_of_element_by_xpath(map.result_text)
            text1 = verify_result.text
            price = self.driver.get_element_by_xpath(map.max_price_drp)
            filter_price = Select(price)
            filter_price.select_by_visible_text("₹20000")
            verify_result = self.driver.get_presence_of_element_by_xpath(map.result_text)
            if text1 != verify_result.text:
                print("filter successful")
            products = self.driver.get_element_by_xpath(map.products_list)
            time.sleep(10)
        except Exception as ex:
            return False
            # print(ex)
            # self.driver.capture_screenshot("ok")
            # raise Exception(ex)

