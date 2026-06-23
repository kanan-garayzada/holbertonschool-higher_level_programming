#!/usr/bin/python3
"""
Sends a POST request to the search_user API with the letter q.
Handles JSON response and prints the user id and name if available.
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(
                response_json.get("id"),
                response_json.get("name")
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
