import os

class Config:
    def __init__(self):
        self.ENDPOINT = os.environ.get('ENDPOINT', 'http://127.0.0.1:8545') # base endpoint
	
        if 'https' in self.ENDPOINT:
            pass
        elif 'http' not in self.ENDPOINT:
            self.ENDPOINT = 'http://'+ self.ENDPOINT

        self.FLASK_PORT = os.environ.get('FLASK_PORT', 5000) # metrics port
