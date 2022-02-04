from flask import Flask, request
from pyfiglet import Figlet
import requests
import logging
import sys
import os


h = Figlet(font="slant")
print(h.renderText("HTTP CHAT"))
print(" 1. Server\n 2. Client\n 3. Exit\n")

user_choice = input("Select mode: ")


def server(ip,port):

    app = Flask(__name__)

    print('\nRunning on http://%s:%s/ (Press CTRL+C to quit)' % (ip,port))

    logging.getLogger("werkzeug").disabled = True
    os.environ["WERKZEUG_RUN_MAIN"] = "true"
    @app.route('/', methods=['GET', 'POST'])
    def chat():
        request_data = request.json
        print(request_data)
        return request_data
    
    app.run(debug=True, port=port, use_reloader=False, host=ip)
    print('\nGoodbye!')
    

def client(ip,port):
        
        username = input("Enter username:")
        print('=====[TO EXIT CTRL+C]=====')
        while True:
            data = input('Message: \n')
            requests.post(url='http://%s:%s' % (ip,port), json='[%s] - %s' % (username,data))
        


if user_choice == '1':
    server(sys.argv[1],sys.argv[2])
    
if user_choice == '2':
    try:
        client(sys.argv[1], sys.argv[2])
    except requests.exceptions.ConnectionError:
        print('Server is not available!')
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit()
    except Exception as e:
        print('We have error!')
        print('Details: %s' % (e))

if user_choice == '3':
    sys.exit()

