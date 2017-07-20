# OutOfMilk Appium automation test sample

import os
import unittest

from appium import webdriver

from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from time import sleep



class OutOfMilkAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = 'AndroidTestDevice'
        desired_caps['app'] = os.path.join(os.getcwd(), 'apps/com.capigami.outofmilk.apk')

        desired_caps['appPackage'] = 'com.capigami.outofmilk'        
        desired_caps['appActivity'] = '.MainActivity'        

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.action = TouchAction(self.driver)


    def tearDown(self):        
        self.driver.quit()

    def test_add_delete_shopping_list_item(self):
        sleep(2)        

        # click the Skip button on Login page
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'action_skip')]").click()                
        
        sleep(2)
        try:
            self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'input_field')]")            
        except NoSuchElementException:
            # maybe because the "What's new message appears", so we need to close the dialog
            self.driver.back()

        el_input = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'input_field')]")
        # input "sugar" into Add Item
        el_input.send_keys("sugar")

        # tap to show the onscreen keyboard
        self.action.tap(el_input).perform()

        # press "Done" button on keyboard
        self.driver.keyevent(66)
            
        sleep(5)

        # check the check box
        self.driver.find_element_by_xpath("//android.widget.CheckBox[contains(@resource-id, 'check_box')]").click()

        # click Delete All button
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id, 'action_delete_all')]").click()

        # confirm Delete All
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id, 'button1')]").click()
        sleep(5)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OutOfMilkAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)