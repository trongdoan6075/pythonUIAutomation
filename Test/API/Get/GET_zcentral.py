import pytest,time, unittest, requests, json

@pytest.mark.usefixtures("set_up") #this mean set_up class in this class will run first
class GET_zcentral(unittest.TestCase):
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
    def test_001_QA(self):
        headers = {
            'Referer': "https://qa.zcentral.zspace.com/search"                    # this is Header. In some case, this can be the authorization
        }
        response = requests.request("GET", self.url, data=[], headers=headers)    # This is where to make the api call. This can be modified to GET, POST, UPDATE, DEL
        print(response.status_code)                                               # This returns the HTTP CODE such as 200, 301, 404, 504 etc.
        res = json.loads(response.text)                                           # Load the response as text to the json format
        print(res)                                                                # Print out the json

    def test_002_Get_check_fields(self):
        # this is Header for most API.
        # In some case, this could be Authenticated credential
        headers = {
            'Referer': "https://qa.zcentral.zspace.com/search"
        }
        # data here is not being used.
        # In most case, it will be used when we need to POST some data
        # data = {}
        response = requests.request("GET", self.url, data=[], headers=headers)       # this is the actual request, similar to curl call
        res = json.loads(response.text)                                              # in this case, reponse is text format, this function will converted into json format
        print("res")
        assert response.status_code == 200                                           # Check http return code from an api call (there will be negative test cases that return : 403, 404, 504 etc...
        assert res["backEndVersion"] == "1.9.6.0.ac6e7b8"                            # res after load json, is now like array/key value pair. You can pull out any key/value by setting the same format here.
        assert res["contentTypes"] == ['ACTIVITY', 'APPLICATION', 'MODEL', 'SIMULATION', 'WEB_LINK']
        assert res["imagePathCDN"] == "https://s3.us-east-2.amazonaws.com/zcentral-images/"
        assert res["uploadsPathCDN"] == "https://zspace-community.s3.amazonaws.com"
        assert res["region"] == "US"
        assert res["cognitoDomain"] == ".zspace.com"

        self.json_validator(response.text)                                           # this is to call another method inside this class. This will call json_validator method down below

    # this method is not running unless you call it like above
    # This method is checking whether or not the returned json is a valid/invalid json
    def json_validator(self, data):
        try:
            json.loads(data)
            return True
        except ValueError as error:
            print("invalid json: %s" % error)
            return False