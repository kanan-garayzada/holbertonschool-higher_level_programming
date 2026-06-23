#!/usr/bin/python3
"""
Uses GitHub API with Basic Authentication to display user id.
The username is sys.argv[1], the password (token) is sys.argv[2].
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        user_data = response.json()
        print(user_data.get("id"))
    except ValueError:
        print(None)
