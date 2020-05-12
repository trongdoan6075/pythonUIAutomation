from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pytest,time, unittest, pyautogui


def browserChrome(self):
    print("Setting up test. Any prerequisite need to define")
    driver = None
    # this is path to chrome driver that help us to start the chrome browser.
    # There is many type of drivers: chrome, firefox, ie, safari, mobile
    driver_path = "C:/qaAuto/zSpace/driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.maximize_window()
    return driver


