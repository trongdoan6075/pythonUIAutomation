import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    @classmethod

    def setUpClass(self):
        # create a new Firefox session
        driver_path = "C:/qaAuto/zSpace/driver/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=driver_path)
        #inst.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        #self.driver.get("http://www.google.com/")
        self.driver.title

    def test_001_search_by_text(self):
        # get the search textbox
        self.driver.get("http://www.google.com/")

    def test_002_search_by_name(self):
        # get the search textbox
        self.driver.get("http://www.yahoo.com/")

    @classmethod
    def tearDownClass(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()