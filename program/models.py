""" Class for Web Pages defined in config file.
Contains: Page url, Page content.
Methods tests and updates data.
"""
from datetime import datetime

class Page:
    def __init__(self, url, content, response):
        self.content = content
        self.log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.url = url
        self.resp_time = ''
        self.status = ''
		# response - dict(url, content, error (if exist), resp_time(if exist))
        self.response = response
    
    def __str__(self):
        return f"{self.log_time} {self.url} {self.status} {self.resp_time}"
    
    def content_is_fulfilled(self):
        if self.content == "":
            self.status = """
                 Content Error: content requirements were not fulfilled
                 """
            return False
        else:
            return True

    def url_is_fulfilled(self):
        if self.url == "":
            self.status = "Url Error: url was not fulfilled"
            self.url = '-'
            return False
        else:
            return True
    
    def is_content_valid(self):
        if self.content in self.response['content']:
            self.status = 'OK'
        else:
            self.status = 'Invalid Content Error'
            return False
    
    def is_response_valid(self):
        if 'error' in self.response:
            self.status = self.response['error']
            return False
        else:
            return True
        
    def is_valid(self):
        return (self.url_is_fulfilled() and self.content_is_fulfilled()
                and self.is_response_valid())
      
    def load_resp_time(self):
        if 'resp_time' in self.response:
            self.resp_time = self.response['resp_time']
           
    def kill(self):
        del self