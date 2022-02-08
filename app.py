from flask import Flask, request
from pyfiglet import Figlet
import requests
import logging
import sys
import os



def hello():
    h = Figlet(font="slant")
    print(h.renderText("HTTP CHAT"))


if len(sys.argv) == 2:
    app = Flask(__name__)

    hello()
    print('Listening on port %s (Press CTRL+C to quit)' % str(sys.argv[1]))

    logging.getLogger("werkzeug").disabled = True
    os.environ["WERKZEUG_RUN_MAIN"] = "true"

    @app.route('/', methods=['GET', 'POST'])
    def chat():
        if request.method == 'POST':
            request_data = request.get_json(force=True)
            print(request_data)
        return request_data
    app.run(port=sys.argv[1], host='0.0.0.0',use_reloader=False)
    print('\nGoodbye!')
    
elif len(sys.argv) == 3:
    try:
        hello()
        username = input("Enter username:")
        print('=====[TO EXIT CTRL+C]=====')
        while True:
            data = input('Message: \n')
            r = requests.post(url='http://%s:%s/' % (sys.argv[1],sys.argv[2]), json='[%s] - %s' % (username,data))
    except requests.exceptions.ConnectionError as e:
        print('Server is not available!')
        print(e)
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit()
    except Exception as e:
        print('We have error!')
        print('Details: %s' % (e))








