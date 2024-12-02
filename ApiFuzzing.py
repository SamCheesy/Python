#API fuzzing reffers to the process of testing an API (Aplication Programming Interface) by sending random,
#invalid, or unexpected inputs (known as "fuzz" data) to identify potential vulnerabilities, bugs, or
#weaknesses in the API.

import requests
import sys

def loop():
    for word in sys.stdin:
        res = requests.get(url="http://10.10.11.161/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
        print(res.status_code)
        print(word)


loop()

