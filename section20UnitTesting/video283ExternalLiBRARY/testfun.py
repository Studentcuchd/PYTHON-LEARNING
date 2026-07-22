from unittest import TestCase,main
from unittest.mock import patch
from classapi import apitest

class TestingApi(TestCase):
    def setUp(self):
        self.api_obj=apitest("https://google.com")  
        
    
    def test_api_mock(self):
        with patch("classapi.requests.get") as mocked_test:
            response=self.api_obj.getting_result()
            print(response)
            mocked_test.assert_called()
            
            
            
"""  
Main part: patch()
with patch("classapi.requests.get") as mocked_get:

Iska matlab:

classapi.py ke andar jo requests.get use ho raha hai, temporarily usko fake Mock object se replace kar do.




Before patch:

requests.get()
     ↓
Real API call

During patch:

requests.get()
     ↓
Mock object
     ↓
No real API call

"""

if __name__=="__main__":
    main()