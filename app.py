from flask import Flask, request
from utils import open_file, generate_fake_users
import requests

app = Flask(__name__)

@app.route('/requirements/')
def open_a_file():
        return open_file()


@app.route('/generate_users/')
def generate_users():

    users_number = request.args.get('users_number', '100')
    users_number = int(users_number)
    return generate_fake_users(users_number)

@app.route('/space/')

def generate_astronaut_number():

    response = requests.get('http://api.open-notify.org/astros.json')
    number = response.json()['number']

    return f'In space: {number}'

if __name__ == '__main__':
    app.run()
