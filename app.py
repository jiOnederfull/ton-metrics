from flask import Flask, render_template
from web3 import Web3
from config import Config

app = Flask(__name__)

# endpoint = Config.ENDPOINT
# flask_port = Config.FLASK_PORT

config = Config()
endpoint = config.ENDPOINT
flask_port = config.FLASK_PORT

w3 = Web3(Web3.HTTPProvider(endpoint))

@app.route('/')
def hello_world():
    return 'This is metrics page of Base.'


@app.route('/metrics')
def metrics():
    block_number = w3.eth.block_number
    return f"chain_head_block {block_number}"


if __name__ == '__main__':
    app.run('0.0.0.0', port=flask_port)
