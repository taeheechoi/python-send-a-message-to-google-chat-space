# Reference https://developers.google.com/chat/quickstart/incoming-bot-python

from json import dumps

from httplib2 import Http

def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = '<INCOMING-WEBHOOK-URL> '
    bot_message = {'text' : 'Hello from a Python script!'}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

if __name__ == '__main__':
    main()