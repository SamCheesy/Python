#API fuzzing reffers to the process of testing an API (Aplication Programming Interface) by sending random,
#invalid, or unexpected inputs (known as "fuzz" data) to identify potential vulnerabilities, bugs, or
#weaknesses in the API.

import requests # type: ignore
import sys

def loop():
    url_inp = input("Enter the url of the API: ")
    for word in sys.stdin:
        res = requests.get(url="{url_inp}/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
        print(res.status_code)
        print(word)


loop()

