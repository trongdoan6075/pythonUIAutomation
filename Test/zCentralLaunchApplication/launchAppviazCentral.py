import pytest,time, unittest, os, keyboard
from keyboard import press
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome

@pytest.mark.usefixtures("set_up")
class GET_zcentral(unittest.TestCase):
    driver = None
    @classmethod
    @pytest.fixture(scope='class')
    def set_up(self):
        print ("Starting to run test requirement")
        # Set url end point
        self.driver_path = "C:/Users/zSpace/PycharmProjects/zCentral/driver/chromedriver.exe"

    def test_001_launch_newton_cradle_analytic_app(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        action = ActionChains(self.driver)
        ''' 
        try:
             self.driver.get("https://qa.zcentral.zspace.com/search")                                                                                                       # Navigate to QA zcentral
             time.sleep(5)
             WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/app-root/div/search/div/div[1]/div[2]/p[1]")))                # Wait 5s for the Filter text
             WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))    # Wait 5s for Input text search box
             input_element1 = self.driver.find_element_by_xpath(( "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))                                    # Initialize input search box element
             input_element1.clear()                                                                                                                                         # this will clear the text box
             input_element1.send_keys("Newton's Cradle - Analytical")                                                                                                       # Send studio keyword to input search box element
             keyboard.press_and_release('enter')                                                                                                                            # This is to press the key ENTER, this can be change to any key from keyboard
             time.sleep(5)                                                                                                                                                  # wait for 5 seconds for the zcentral to complete searching
             moveoverElement = self.driver.find_element_by_xpath("//p[contains(.,'Interactive STEM simulation.')]")                                                         # locate Newton's Cradle - Analytical result
             action.move_to_element(moveoverElement).perform()                                                                                                              # This hovers the mouse over the the Newton's Cradle - Analytical
             time.sleep(5)
             self.driver.find_element_by_css_selector("#\\34 4ff2b3c-b692-4d83-8012-9c8b0e071f90 .item-overlay-icon .svg-inline--fa").is_displayed()                        # This is to check if the launch square button is existed
             self.driver.find_element_by_css_selector("#\\34 4ff2b3c-b692-4d83-8012-9c8b0e071f90 .item-overlay-icon .svg-inline--fa").click()                               # Click on the launch button
             time.sleep(10)
        '''
        myCmd = 'tasklist | findstr "tasklist.exe" '
        os.system(myCmd)
        '''
        finally:
             self.driver.close()
        '''
