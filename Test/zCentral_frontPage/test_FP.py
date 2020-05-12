from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pytest, time, unittest, pyautogui


# from browsermobproxy import Server

@pytest.mark.usefixtures("set_up")  ### set_up method will execute first
class zCentral_frontPage(unittest.TestCase):
    driver = None

    @classmethod
    @pytest.fixture(scope='class')
    # This method will be used if you need to set any variable before executing any test cases
    # More like prerequisite
    def set_up(self):
        print("Setting up test. Any prerequisite need to define")
        # this is path to chrome driver that help us to start the chrome browser.
        # There is many type of drivers: chrome, firefox, ie, safari, mobile
        self.driver_path = "C:/qaAuto/zSpace/driver/chromedriver.exe"

    def test_001_QA_zCentral_search_Studio(self):
        # This is the way to launch chrome browser from loading the chrome driver path in set_up class above
        # options = webdriver.ChromeOptions()          # To define chrome option such as: enable developer tools, ignore ssl , etc.
        # options.add_argument("--start-maximized")    # This action is to maximize the window
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        try:
            print("Testing Search feature from Search Box ...")
            self.driver.get("https://qa.zcentral.zspace.com/search")  # Navigate to QA zcentral
            time.sleep(10)  # wait for 10 second for the page to start loading
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//header[@id='header_1']/div[2]/app-search-widget")))  # Wait 5s for the Filter text on the left side in UI
            input_element1 = self.driver.find_element_by_xpath(("//header[@id='header_1']/div[2]/app-search-widget"))  # Find input search box element
            input_element1.send_keys("Studio")  # Send "studio" keyword to input search box element
            input_element1.send_keys(Keys.ENTER)
            #pyautogui.hotkey('ENTER')
            time.sleep(3)
            # WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".content-results > p:nth-child(1)")))
            # WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//p[contains(.,'Results: 8 Results Found')]")))
            # WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/app-root/div/app-content/section/div/p[1]")))
            # result = self.driver.find_element_by_css_selector(".content-results > p:nth-child(1)").text
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".content-results > p:nth-child(1)")))
            result = self.driver.find_element_by_css_selector(".content-results > p:nth-child(1)").text
            assert result == "Results: 8 Results Found"
        finally:
            self.driver.close()  # This is to close the chrome after this run.

    def test_002_QA_zCentral_search_Studio_Franklin_Invalid(self):
        # This is the way to launch chrome browser from loading the chrome driver path in set_up class above
        # options = webdriver.ChromeOptions()          # To define chrome option such as: enable developer tools, ignore ssl , etc.
        # options.add_argument("--start-maximized")    # This action is to maximize the window
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        try:
            print("Testing Search feature from Search Box ...")
            self.driver.get("https://qa.zcentral.zspace.com/search")  # Navigate to QA zcentral
            time.sleep(10)  # wait for 10 second for the page to start loading
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//header[@id='header_1']/div[2]/app-search-widget")))  # Wait 5s for the Filter text on the left side in UI
            input_element1 = self.driver.find_element_by_xpath(("//header[@id='header_1']/div[2]/app-search-widget"))  # Find input search box element
            input_element1.send_keys("Studio")  # Send "studio" keyword to input search box element
            pyautogui.hotkey('ENTER')
            time.sleep(3)
            # WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//header[@id='header_1']/div[2]/app-search-widget")))  # Wait 5s for the Filter text on the left side in UI
            input_element2 = self.driver.find_element_by_xpath(("//header[@id='header_1']/div[2]/app-search-widget"))  # Find input search box element
            print("Searching for Franklin search string ...")
            input_element2.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE,Keys.BACKSPACE)
            time.sleep(2)
            input_element2.send_keys("Franklin")  # Send search string keyword to input search box element
            time.sleep(5)
            pyautogui.hotkey('ENTER')
            time.sleep(2)
            # WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,"//header[@id='header_1']/div[2]/app-search-widget")))  # Wait 5s for the Filter text on the left side in UI
            input_element3 = self.driver.find_element_by_xpath(
                ("//header[@id='header_1']/div[2]/app-search-widget"))  # Find input search box element
            input_element3.send_keys(Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACKSPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
            time.sleep(2)
            print("Search for none existing product name from search box .......")
            input_element3.send_keys("THISISZSPACE")  # Send "studio" keyword to input search box element
            time.sleep(2)
            pyautogui.hotkey('ENTER')
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".content-results > p:nth-child(1)")))
            result = self.driver.find_element_by_css_selector(".content-results > p:nth-child(1)").text
            assert result == "Results: 0 Results Found"
        finally:
            self.driver.close()

    def test_003_QA_zCentral_Navigate_Pages(self):
        # This is the way to launch chrome browser from loading the chrome driver path in set_up class above
        #options = webdriver.ChromeOptions()          # To define chrome option such as: enable developer tools, ignore ssl , etc.
        #options = Options()
        #options.add_argument("user-data-dir=C:\\Users\\zSpace\\AppData\\Local\\Google\\Chrome\\User Data\\Default")    # This action is to maximize the window
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        try:
            self.driver.get("https://qa.zcentral.zspace.com/search")  # Navigate to QA zcentral
            time.sleep(10)
            # wait for 10 second for the page to start loading
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".fa-cog")))
            self.driver.find_element_by_css_selector(".fa-cog").click()  # click on settings icon
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".fa-question-circle")))
            self.driver.find_element_by_css_selector(".fa-question-circle").click()  # click on HELP
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".fa-info-circle")))
            self.driver.find_element_by_css_selector(".fa-info-circle").click()  # click on About
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".fa-th")))
            self.driver.find_element_by_css_selector(".fa-th").click()  # click on Application launcher
            time.sleep(2)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".apps-close")))
            self.driver.find_element_by_css_selector(".apps-close").click()  # close APP LIST
            time.sleep(3)
            self.driver.refresh()
            time.sleep(10)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//header[@id='header_1']/div[2]/app-search-widget")))  # Wait 5s for the Filter text on the left side in UI
            input_element1 = self.driver.find_element_by_xpath(("//header[@id='header_1']/div[2]/app-search-widget"))  # Find input search box element
            input_element1.send_keys("Studio")  # Send "studio" keyword to input search box element
            pyautogui.hotkey('ENTER')
            time.sleep(3)

            ''' 
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/app-root/div/app-content/section/virtual-scroller/div[2]/app-content-tile[1]/div/div/div[1]/div[2]/p[2]")))
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-content/section/virtual-scroller/div[2]/app-content-tile[1]/div/div/div[1]/div[2]/p[2]").click()
            for x in range(0, 500):
                pyautogui.hotkey('down')

            time.sleep(3)
            '''
        finally:
            self.driver.close()  # This is to close the chrome after this run.

    def noRun_101_PRODUCTION_zCentral_search_Studio(self):
        # This is the way to launch chrome browser from loading the chrome driver path in set_up class above
        # options = webdriver.ChromeOptions()          # To define chrome option such as: enable developer tools, ignore ssl , etc.
        # options.add_argument("--start-maximized")    # This action is to maximize the window
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        try:
            self.driver.get("https://go.zspace.com/search")  # Navigate to QA zcentral
            time.sleep(10)  # wait for 10 second for the page to start loading
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                       "/html/body/app-root/div/search/div/div[1]/div[2]/p[1]")))  # Wait 5s for the Filter text on the left side in UI
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                       "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))  # Wait 5s for Input text search box
            input_element1 = self.driver.find_element_by_xpath(
                ("//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))  # Find input search box element
            input_element1.send_keys("Studio")  # Send "studio" keyword to input search box element
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                       "//*[@id=\"suggestion_list\"]/li[1]")))  # Wait for drop down after sending keyword to input search box
            self.driver.find_element_by_xpath(
                "//*[@id=\"suggestion_list\"]/li[1]").click()  # Click on the target element drop down (this one is the first one from drop down)
            time.sleep(5)  # wait for 5 seconds
            # When you search for the string studio, zcentral will show the number of results
            # So, locate the element then .text is to get the text our of that element. Compare to expected result
            assert self.driver.find_element_by_xpath(
                "//div[@id='search_right_content']/div/div").text == "1 Results Found"
        finally:
            self.driver.close()  # This is to close the chrome after this run.

    def noRUn_102_PRODUCTION_repeat_search(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.maximize_window()
        try:
            self.driver.get("https://go.zspace.com/search")  # Navigate to QA zcentral
            time.sleep(10)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(
                (By.XPATH, "/html/body/app-root/div/search/div/div[1]/div[2]/p[1]")))  # Wait 5s for the Filter text
            for x in range(1):  # Loop reason: if we need to run more than one
                WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                           "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))  # Wait 5s for Input text search box
                input_element1 = self.driver.find_element_by_xpath((
                                                                       "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))  # Initialize input search box element
                input_element1.clear()  # this will clear the text box
                input_element1.send_keys("studio")  # Send studio keyword to input search box element
                WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                           "//*[@id=\"suggestion_list\"]/li[1]")))  # Wait for drop down after sending keyword to input search box
                self.driver.find_element_by_xpath(
                    "//*[@id=\"suggestion_list\"]/li[1]").click()  # Click on the target element drop down
                time.sleep(5)  # wait for 5 seconds
                WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                           "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))  # Wait 5s for Input text search box
                input_element1 = self.driver.find_element_by_xpath((
                                                                       "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))  # Initialize input search box element
                input_element1.clear()  # this will clear the text box
                input_element1.send_keys("Franklin")  # Send studio keyword to input search box element
                WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                           "//*[@id=\"suggestion_list\"]/li[1]")))  # Wait for drop down after sending keyword to input search box
                self.driver.find_element_by_xpath(
                    "//*[@id=\"suggestion_list\"]/li[1]").click()  # Click on the target element drop down
                time.sleep(5)  # wait for 5 seconds
                WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                           "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))  # Wait 5s for Input text search box
                input_element1 = self.driver.find_element_by_xpath((
                                                                       "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))  # Initialize input search box element
                input_element1.clear()  # this will clear the text box
                input_element1.send_keys("IOT")  # Send studio keyword to input search box element
                pyautogui.hotkey('ENTER')  # This is the method to invoke any keyboard. I am pressing ENTER in this case
                time.sleep(5)
                assert self.driver.find_element_by_xpath(
                    "//div[@id='search_right_content']/div/div").text == "0 Results Found"  # Check if the result returns correctly
                time.sleep(5)  # wait for 5 seconds
        finally:
            self.driver.close()

    ''' 
    def notRun_Staging(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        try:
            self.driver.get("https://staging.zcentral.zspace.com/search")                                                                                                       # Navigate to QA zcentral
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/app-root/div/search/div/div[1]/div[2]/p[1]")))                     # Wait 5s for the Filter text
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))        # Wait 5s for Input text search box
            input_element1 = self.driver.find_element_by_xpath(("//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))                                          # Initialize input search box element
            input_element1.send_keys("studio")                                                                                                                                  # Send studio keyword to input search box element
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=\"suggestion_list\"]/li[1]")))                                        # Wait for drop down after sending keyword to input search box
            self.driver.find_element_by_xpath("//*[@id=\"suggestion_list\"]/li[1]").click()                                                                                     # Click on the target element drop down
            time.sleep(5)                                                                                                                                                       # wait for 5 seconds

            # Chose your own assert here
            # find any element on the UI and assert it.

        finally:
            self.driver.close()

        '''
    '''
    def test_QA_turn_on_developer_tool_to_collect_data(self):
        # This is the way to launch chrome browser from loading the chrome driver path in set_up class above

        server = Server('C:/qaAuto/zCentral/browsermob-proxy-2.1.4/bin/browsermob-proxy')
        server.start()
        proxy = server.create_proxy()

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('auto-open-devtools-for-tabs')
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)

        self.driver.get("https://qa.zcentral.zspace.com/search")  # Navigate to QA zcentral
        time.sleep(5)
        self.driver.get("https://qa.zcentral.zspace.com/search")  # Navigate to QA zcentral
        time.sleep(5)
        self.driver.get("https://qa.zcentral.zspace.com/search")  # Navigate to QA zcentral
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'shift', 'i')
        time.sleep(10)
        print("going to hit Control + e to record .....")
        pyautogui.hotkey('ctrl', 'e')
        time.sleep(20)


        time.sleep(10)                                                 # wait for 10 second for the page to start loading
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/app-root/div/search/div/div[1]/div[2]/p[1]")))             # Wait 5s for the Filter text on the left side in UI
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))# Wait 5s for Input text search box
        input_element1 = self.driver.find_element_by_xpath(("//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))                                  # Find input search box element
        input_element1.send_keys("studio")                                                                                                                          # Send "studio" keyword to input search box element
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=\"suggestion_list\"]/li[1]")))                                # Wait for drop down after sending keyword to input search box
        self.driver.find_element_by_xpath("//*[@id=\"suggestion_list\"]/li[1]").click()                                                                             # Click on the target element drop down (this one is the first one from drop down)
        time.sleep(5)                                                                                                                                               # wait for 5 seconds
        # When you search for the string studio, zcentral will show the number of results
        # So, locate the element then .text is to get the text our of that element. Compare to expected result
        assert self.driver.find_element_by_xpath("//div[@id='search_right_content']/div/div").text == "2,420 Results Found"
    '''

    ''' 
    def tearDown(self):
        print("This is TEARNDOWN function .......")
        self.driver.quit()
    '''
