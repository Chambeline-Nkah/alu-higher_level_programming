
'''Script that takes in a URL, sends a request to it and 
- displays the body of the response'''


import sys
import requests


if __name__ == "__main__":
    """send the email"""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code <= 400:
        print("{}".format(response.text))
    else:
        print("Error code: {}".format(response.status_code))
