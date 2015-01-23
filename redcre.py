# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Redcre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.reddit.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_redcre(self):
        driver = self.driver

        # # time.sleep(700)

        # driver.get(self.base_url + "/")
        # driver.find_element_by_link_text("sign in or create an account").click()
        # driver.find_element_by_id("user_reg").click()
        # driver.find_element_by_id("user_reg").clear()
        # driver.find_element_by_id("user_reg").send_keys("XXXXXXX")
        # driver.find_element_by_id("passwd_reg").clear()
        # driver.find_element_by_id("passwd_reg").send_keys("XXXXXXX")
        # driver.find_element_by_id("passwd2_reg").clear()
        # driver.find_element_by_id("passwd2_reg").send_keys("XXXXXXX")
        # driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        # driver.find_element_by_link_text("logout").click()
    
        time.sleep(700)

        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("sign in or create an account").click()
        driver.find_element_by_id("user_reg").click()
        driver.find_element_by_id("user_reg").clear()
        driver.find_element_by_id("user_reg").send_keys("XXXXXXX")
        driver.find_element_by_id("passwd_reg").clear()
        driver.find_element_by_id("passwd_reg").send_keys("XXXXXXX")
        driver.find_element_by_id("passwd2_reg").clear()
        driver.find_element_by_id("passwd2_reg").send_keys("XXXXXXX")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_link_text("logout").click()
    


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
