import pytest,time, unittest, requests, json, os
from subprocess import check_output
import subprocess

@pytest.mark.usefixtures("set_up") #this mean set_up class in this class will run first
class Appmanager_install_Package_Check_Automation(unittest.TestCase):
    driver = None
    @classmethod
    @pytest.fixture(scope='class')
    ## This set_up method always before any test run.
    def set_up(self):
        print ("Starting to run test requirement")
        # Set url end point
        self.url = "https://qa.zcentral.zspace.com/api/v1/content-meta-bundle48737ec339d29f7be63a0b87081331d70ae109d?language=en-US"   # this is your API end point

    # which ever method that has the string "test" will be your test case and only these will be run
    # This is part of the pytest framework


    def test_001_install_zSpace_Tennis(self):
        print("Going to download and install Tennis App")
        if (os.path.exists('C:/Program Files (x86)/zSpace/zSpaceTennis')):
            print("Going to delete the app")
            check_output("\"C:/Program Files/zspace/App Manager/zspace_appmanager.exe\" --silent --remove=tennis --debug\"", shell=True)
            i=0
            while i < 120:
                print("Checking until App Manager disappears from background")
                time.sleep(1)
                amservice = os.system('tasklist | findstr zspace_appmanager.exe')
                if amservice == 1:
                    print("Found App Manager Service stop Running")
                    i = 120

        os.system("@echo Started: %date% %time%")
        check_output("\"C:/Program Files/zspace/App Manager/zspace_appmanager.exe\" --silent --install=tennis --debug", shell=True)
        print(check_output)
        x=0
        while x < 120:
            print("Checking until App Manager disappears from background")
            time.sleep(1)
            amservice = os.system('tasklist | findstr zspace_appmanager.exe')
            if amservice == 1:
                print("App Manager Service stop Running")
                x = 120
        os.system("@echo Started: %date% %time%")
        print("DOWNLOADING TENNIS IS DONE ...")

    def test_001_install_Tennis_Dir_exist(self):
        print("check if Tennis Directory get created after installation")
        result = os.path.exists('C:/Program Files (x86)/zSpace/zSpaceTennis')
        assert True == result

    def test_002_install_Tennis_number_of_files(self):
        print("total number of file from Tennis application")
        cpt= sum([len(files) for r, d, files in os.walk("C:/Program Files (x86)/zSpace/zSpaceTennis")])
        assert 69 == cpt

    def test_003_install_Tennis_check_log_generated(self):
        print("Check if Log gets generated")
        result = os.path.exists('C:/Users/zSpace/Desktop/host.developer.log')
        assert True == result

    def test_004_install_Tennis_launch_app(self):

        print("Launching the Tennis")
        subprocess.Popen("C:/Program Files (x86)/zSpace/zSpaceTennis/zSpaceTennis.exe", close_fds=True)
        time.sleep(5)
        print("THIS IS TESTING")
        tennisservice = check_output("tasklist | findstr zSpaceTennis.exe", shell=True)
        assert "zSpaceTennis.exe" in str(tennisservice)
        print("Killing Tennis Process")
        check_output("taskkill /IM zSpaceTennis.exe", shell=True)



    def test_001_install_curieselements(self):
        
        assert True

    def test_002_install_vivedScience(self):
        
        assert True

    def test_003_install_gta_industrial_robotics_mechenic(self):
        
        assert True

    def test_004_install_virtual_ECG(self):
        
        assert True

    def test_005_install_zcentral(self):
        
        assert True

    def test_006_install_zcentral(self):
        
        assert True

    def test_007_install_zcentral(self):
        
        assert True

