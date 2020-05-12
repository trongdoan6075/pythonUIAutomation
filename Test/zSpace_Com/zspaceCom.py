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
#from common.broswerDriver import *
# from browsermobproxy import Server

@pytest.mark.usefixtures("set_up") ### set_up method will execute first
class zSpace_Com(unittest.TestCase):
    driver = None
    @classmethod
    @pytest.fixture(scope='class')
    # This method will be used if you need to set any variable before executing any test cases
    # More like prerequisite
    def set_up(self):
         print("This is inital set up")
         #self.driver = browserChrome(self)

         self.driver_path = "C:/qaAuto/zSpace/driver/chromedriver.exe"

    def test_001_Check_Link_ribbon(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.get("https://zspace.com")
        assert self.driver.find_element_by_xpath("//img[@alt='zSpace Logo']")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'PURCHASE')]")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'DEVELOPER SITE')]")
        assert self.driver.find_element_by_xpath("//a[contains(text(),'EDUCATOR RESOURCES')]")
        assert self.driver.find_element_by_xpath("//span[contains(.,'SUPPORT')]")
        assert self.driver.find_element_by_xpath("//span[contains(.,'SIGN IN')]")

    def test_002_check_product_link_to_technology(self):
        #self.driver = browserChrome(self)
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.get("https://zspace.com")
        self.driver.find_element_by_xpath("//a[contains(text(),'PRODUCT')]").click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//a[contains(text(),'Technology')]")))
        self.driver.find_element_by_xpath("//a[contains(text(),'Technology')]").click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//h2[contains(.,'Behind the Magic of zSpace')]")))

        assert self.driver.find_element_by_xpath("//h2[contains(.,'Behind the Magic of zSpace')]").text == "Behind the Magics of zSpace"


    def test_003_check_first_text(self):
        #self.driver = browserChrome(self)
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.get("https://zspace.com")
        assert self.driver.find_element_by_xpath("//div[2]/div/div[2]/div").text == "Learning Through AR / VR Experiences\nSee it to believe it\nLEARN MORE\nContact Sales  "

    def test_004_check_external_link_img(self):
        #self.driver = browserChrome(self)
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.get("https://zspace.com")
        assert self.driver.find_element_by_xpath("//img[@alt='Forbes']")
        assert self.driver.find_element_by_xpath("//img[@alt='Scholastic']")
        assert self.driver.find_element_by_xpath("//img[@alt='Los Angeles Times']")
        assert self.driver.find_element_by_xpath("//img[@alt='The Journal']")
        assert self.driver.find_element_by_xpath("//img[@alt='Fortune']")

    def test_005_check_Valyada_Lee(self):
        #self.driver = browserChrome(self)
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        self.driver.get("https://zspace.com")

        assert self.driver.find_element_by_xpath("//p[contains(.,'Valya Lee')]").text == "Valya Lee"
        assert self.driver.find_element_by_xpath("//p[contains(.,'Superintendent')]").text == "Superintendent"
        assert self.driver.find_element_by_xpath("//p[contains(.,'Liberty County School District')]").text == "Liberty County School District"


    def tearDown(self):
        print("This is TEARNDOWN function .......")
        self.driver.quit()
