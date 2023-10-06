from flask import Flask, render_template
from config import Config

import requests

app = Flask(__name__)

# endpoint = Config.ENDPOINT
# flask_port = Config.FLASK_PORT

config = Config()
endpoint = config.ENDPOINT
flask_port = config.FLASK_PORT

#url = 'http://localhost/getMasterchainInfo'
url = endpoint+"/getMasterchainInfo"
headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)


@app.route('/')
def hello_world():
    return 'This is metrics page of TON.'


@app.route('/metrics')
def metrics():
    if response.status_code == 200:
        data = response.json()
        block_number = data['result']['last']['seqno']
        return f"chain_head_block {block_number}"
    else:
        return f'Error: Status code {response.status_code}'


if __name__ == '__main__':
    app.run('0.0.0.0', port=flask_port)
