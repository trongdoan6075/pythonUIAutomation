from locust import HttpLocust, TaskSet, task
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import pytest,time, unittest

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get("https://qa.zcentral.zspace.com")

    @task
    def about(self):
        self.client.get("https://qa.zcentral.zspace.com/search")
        self.client.get("https://qa.zcentral.zspace.com/settings")
        # This is the way to launch chrome browser from loading the chrome driver path in set_up class above
        driver_path = "C:/Users/tdoan/LOCUST/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=driver_path)
        try:
            print("testing start ------------------------------------------------")
            driver.get("https://qa.zcentral.zspace.com/search")       # Navigate to QA zcentral
            time.sleep(10)                                                 # wait for 10 second for the page to start loading
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/app-root/div/search/div/div[1]/div[2]/p[1]")))             # Wait 5s for the Filter text on the left side in UI
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input")))# Wait 5s for Input text search box
            print("Locating Element is done -----------------------------------------")
            input_element1 = driver.find_element_by_xpath(("//div[@id='header_2']/div[2]/form/mat-form-field/div/div/div/input"))                                  # Find input search box element
            input_element1.send_keys("studio")                                                                                                                          # Send "studio" keyword to input search box element
            print("Sending search keyword --------------------------------------------")
            WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id=\"suggestion_list\"]/li[1]")))                                # Wait for drop down after sending keyword to input search box
            driver.find_element_by_xpath("//*[@id=\"suggestion_list\"]/li[1]").click()                                                                             # Click on the target element drop down (this one is the first one from drop down)
            print("CLICK ON DROPDOWN -------------------------------------------------")
            time.sleep(5)                                                                                                                                               # wait for 5 seconds
            # When you search for the string studio, zcentral will show the number of results
            # So, locate the element then .text is to get the text our of that element. Compare to expected result
            # assert driver.find_element_by_xpath("//div[@id='search_right_content']/div/div").text == "2,646 Results Found"
            result_test = driver.find_element_by_xpath("//div[@id='search_right_content']/div/div").text
            print(result_test)
        finally:
            driver.close()
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5
    max_wait = 15000
