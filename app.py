from flask import Flask, request
from pyfiglet import Figlet
import requests
import logging
import sys


host = "http://127.0.0.1:8080"

h = Figlet(font="slant")
print(h.renderText("HTTP CHAT"))
print(" 1. Server\n 2. Client\n 3. Exit\n")


user_choice = input("Select mode: ")



def server():
    app = Flask(__name__)

    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    @app.route('/', methods=['GET', 'POST'])
    def chat():
        request_data = request.json
        print(request_data)
        return request_data
    
    app.run(port=8080)

    
def client():
        try:
            username = input("Enter username:")
            print('=====[TO EXIT CTRL+C]=====')
            while True:
                data = input('Message: \n')
                r = requests.post(url=host, json='[%s] - %s' % (username,data))
        except requests.exceptions.ConnectionError:
            print('Server is not available!')
        except KeyboardInterrupt:
            print('\nGoodbye!')
            sys.exit()
        except Exception as e:
            print('We have error!')
            print('Details: %s' % (e))



if user_choice == '1':
    server()

if user_choice == '2':
    client()

if user_choice == '3':
    sys.exit()

