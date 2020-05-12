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

# @pytest.mark.usefixtures("set_up") ### set_up method will execute first
class zSpace_developerSite(unittest.TestCase):
    driver = None
    @classmethod
    # @pytest.fixture(scope='class')
    # This method will be used if you need to set any variable before executing any test cases
    # More like prerequisite
    def set_up(self):
         print("This is inital set up")
         self.driver = browserChrome(self)

    def test_001_Title(self):
        # self.driver = browserChrome(self)
        self.set_up()
        self.driver.get("https://developer.zspace.com")
        assert self.driver.find_element_by_xpath("//h2").text == "Break the Screen Barrier!"
        assert self.driver.find_element_by_xpath("//h6").text == "Developing for the zSpace AR/VR platform means shaping the future of learning and spatial content. " \
                                                                  "Millions of students in thousands of schools use zSpace for virtual experiential learning, giving zSpace " \
                                                                  "the largest reach of any AR/VR learning platform. zSpace is powering spatial content delivery for Learning, " \
                                                                  "Medical and Manufacturing - be a part of the revolution."

    def test_002_Link_HardWare(self):
        # self.driver = browserChrome(self)
        self.set_up()
        self.driver.get("https://developer.zspace.com")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'Request Hardware')]").text == "REQUEST HARDWARE"

    def test_003_Hardware_Image(self):
        # self.driver = browserChrome(self)
        self.set_up()
        self.driver.get("https://developer.zspace.com")
        self.driver.find_element_by_xpath("//div[2]/img")
        if self.driver.find_element_by_xpath("//div[2]/img"):
            assert True

    @classmethod
    def tearDown(self):
        print("This is TEARNDOWN function .......")
        self.driver.quit()
