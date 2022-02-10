from flask import Flask, request
import pyfiglet
import requests
import logging
import sys
import os


logo = pyfiglet.figlet_format('HTTP CHAT', font="slant")


if len(sys.argv) == 2:
    app = Flask(__name__)

    print(logo)
    print('Listening on port %s (Press CTRL+C to quit)' % str(sys.argv[1]))

    logging.getLogger("werkzeug").disabled = True
    os.environ["WERKZEUG_RUN_MAIN"] = "true"

    @app.route('/', methods=['POST'])
    def chat():
        request_data = request.get_data(as_text=True)
        print(request_data)
        return request_data
    app.run(port=sys.argv[1], host='0.0.0.0',use_reloader=False)
    print('\nGoodbye!')
    
elif len(sys.argv) == 3:
    try:
        print(logo)
        username = input("Enter username:")
        print('=====[TO EXIT CTRL+C]=====')
        while True:
            data = input('Message: \n')
            r = requests.post(url='http://%s:%s/' % (sys.argv[1],sys.argv[2]), data='[%s] - %s\n' % (username, data))
    except requests.exceptions.ConnectionError as e:
        print('Server is not available!')
        print(e)
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit()
    except Exception as e:
        print('We have error!')
        print('Details: %s' % (e))








