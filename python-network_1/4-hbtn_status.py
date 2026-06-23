#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
and displays the body of the response with proper formatting.
"""

import requests

response = requests.get("https://intranet.hbtn.io/status")
body = response.text

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
