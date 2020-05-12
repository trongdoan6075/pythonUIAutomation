from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pytest,time, unittest, pyautogui
from common.broswerDriver import *
# from browsermobproxy import Server

@pytest.mark.usefixtures("set_up") ### set_up method will execute first
class zSpace_asia(unittest.TestCase):
    driver = None
    @classmethod
    @pytest.fixture(scope='class')
    # This method will be used if you need to set any variable before executing any test cases
    # More like prerequisite
    def set_up(self):
         print("This is inital set up")
         #self.driver = browserChrome(self)

    def test_001_Check_Link_ribbon(self):
        self.driver = browserChrome(self)
        self.driver.get("https://zspace.asia")
        time.sleep(10)
        assert self.driver.find_element_by_xpath("//img[@alt='zSpace Logo']")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'产品')]")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'应用')]")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'普教')]")
        assert self.driver.find_element_by_xpath("//a[contains(.,'高教')]")
        assert self.driver.find_element_by_xpath("//a[contains(.,'医疗')]")
        assert self.driver.find_element_by_xpath("//a[contains(.,'服务与支持')]")


    def test_002_check_first_text(self):
        self.driver = browserChrome(self)
        self.driver.get("https://zspace.asia")
        time.sleep(10)
        assert self.driver.find_element_by_xpath("//h2").text == "身临其境的学习体验"

    def tearDown(self):
        print("This is TEARNDOWN function .......")
        self.driver.quit()
