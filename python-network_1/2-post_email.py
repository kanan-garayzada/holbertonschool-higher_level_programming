#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the response body decoded in utf-8.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the POST data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a Request object with POST data
    req = urllib.request.Request(url, data=data)

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
