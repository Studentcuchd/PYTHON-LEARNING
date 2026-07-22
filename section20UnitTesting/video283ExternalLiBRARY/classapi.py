import requests

class apitest():
    def __init__(self,url):
        self.url=url
    
    def getting_result(self):
        return requests.get(self.url).content