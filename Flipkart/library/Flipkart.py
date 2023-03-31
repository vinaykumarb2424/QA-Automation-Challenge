import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.join(str(Path(os.getcwd()).parent.parent)))
import time
from common_functionality import *
from map import flipkart as map
from log.log import log_files

logger = log_files("Flipkart")


class Flipkart(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.driver = WebDriver()
        logger.info("webdriver created")

    def close_login_popup(self):
        """
        
        :return:
        """
        try:
            logger.info("login pop up closing")
            close_login = self.driver.get_element_by_xpath(map.close_login_popup)
            if close_login.is_displayed():
                close_login.click()
                logger.info("close pop up clicked")
                time.sleep(5)
                return True
        except Exception as ex:
            return False

    def search_product(self, product_name):
        """

        :param product_name:
        :return:
        """
        try:
            if self.close_login_popup():
                search_product = self.driver.get_element_by_name(map.search_input_by_name)
                search_product.send_keys(product_name)
                logger.info("searching {}".format(product_name))
                search_button = self.driver.get_element_by_xpath(map.search_submit_btn)
                search_button.click()
                logger.info("search Button clicked")
        except Exception as ex:
            raise Exception(ex)

    def verify_product_search(self, product_name):
        """

        :param product_name:
        :return:
        """
        try:
            verify_product_searched = self.driver.get_presence_of_element_by_xpath(map.searched_product_text % product_name)
            if verify_product_searched.is_displayed():
                logger.info("products listed")
                return True
        except Exception as ex:
            return False

    def filter_products(self, price):
        """

        :param price:
        :return:
        """
        try:
            default_text = self.driver.get_presence_of_element_by_xpath(map.result_text).text
            logger.info("default text:{}".format(default_text))
            self.driver.select_from_dropdown_using_text(map.max_price_drp, price)
            time.sleep(5)
            text_after_filter = self.driver.get_presence_of_element_by_xpath(map.result_text).text
            logger.info("text_after_filter:{}".format(text_after_filter))
            if default_text != text_after_filter:
                logger.info("filter successful")
            #time.sleep(10)
        except Exception as ex:
            raise Exception(ex)

    def click_3rd_product(self):
        """

        :return:
        """
        try:
            product_text_before_open = ""
            products = self.driver.get_elements_by_xpath(map.products_list)
            page_title_before = self.driver.get_page_title()
            logger.info("page_title_before: {}".format(page_title_before))
            for index, element in enumerate(products):
                if index == 2:
                    element.click()
                    product_text_before_open = element.text
                    break
            logger.info("product_text_before_open: {}".format(product_text_before_open))
            self.driver.switch_to_window(2)
            page_title_after = self.driver.get_page_title()
            logger.info("page_title_after: {}".format(page_title_after))
            if page_title_before != page_title_after:
                logger.info("product open successful", product_text_before_open)
            else:
                logger.error("product failed to open", product_text_before_open)
                raise Exception("failed view product")
        except Exception as ex:
            raise Exception("failed view product", ex)

    def add_cart(self):
        """

        :return:
        """
        try:
            time.sleep(10)
            self.driver.switch_to_window(2)
            logger.info(self.driver.get_page_title())
            logger.info("window switched")
            self.driver.get_element_by_xpath(map.add_cart).click()
            time.sleep(20)
        except Exception as ex:
            logger.error("cart verification failed")
            raise Exception(ex)

    def verify_cart(self):
        """

        :return:
        """
        try:
            self.driver.page_refresh()
            cart = self.driver.get_presence_of_element_by_xpath(map.cart_number)
            if int(cart.text) >= 1:
                return "cart verified successfully"
        except Exception as ex:
            logger.error("cart verification failed")
            raise Exception(ex)



# s = Flipkart()
# s.search_product("samsung mobiles")
# s.verify_product_search("samsung mobiles")
# s.filter_products()
# s.click_3rd_product()
# s.add_cart()
# print(s.verify_cart())
