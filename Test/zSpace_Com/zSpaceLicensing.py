from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pytest,time, unittest, pyautogui, random, string
# from common.broswerDriver import *
# from browsermobproxy import Server

@pytest.mark.usefixtures("set_up") ### set_up method will execute first
class zSpace_Licensing(unittest.TestCase):
    driver = None
    @classmethod
    @pytest.fixture(scope='class')
    # This method will be used if you need to set any variable before executing any test cases
    # More like prerequisite
    def set_up(self):
         print("This is inital set up")
         self.driver_path = "C:/qaAuto/zSpace/driver/chromedriver.exe"
         #self.driver = browserChrome(self)

    def test_001_Check_Link_ribbon(self):
        # options = webdriver.ChromeOptions()          # To define chrome option such as: enable developer tools, ignore ssl , etc.
        # options.add_argument("--start-maximized")    # This action is to maximize the window
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()

        for x in range(0,2):
            chars = string.ascii_lowercase + string.digits
            testEmail = ''.join(random.choice(chars) for _ in range(15)) + "@test.com"
            password = ''.join(random.choice(chars) for _ in range(15))
            print(testEmail)
            print(password)
            self.driver.get("https://qadmp.zcentral.zspace.com/")
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='auth_email']")))
            input_element1 = self.driver.find_element_by_xpath("//input[@id='auth_email']")  # Find input search box element
            input_element1.send_keys(testEmail)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='auth_password']")))
            input_element2 = self.driver.find_element_by_xpath("//input[@id='auth_password']")  # Find input search box element
            input_element2.send_keys(password)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(.,'Sign In')]")))
            self.driver.find_element_by_xpath("//button[contains(.,'Sign In')]").click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='auth_error']")))
            time.sleep(3)
            assert self.driver.find_element_by_xpath("//div[@id='auth_error']").text == "Invalid credentials"
            self.driver.refresh()

    def tearDown(self):
            print("This is TEARNDOWN function .......")
            self.driver.quit()
