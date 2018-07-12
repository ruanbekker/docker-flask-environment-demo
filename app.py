from flask import Flask
from env_vars import get_owner

app = Flask(__name__)

owner_name = get_owner()

@app.route('/')
def index():
    return 'Hello, World'

@app.route('/owner')
def owner():
    owner_name = get_owner()
    return owner_name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
