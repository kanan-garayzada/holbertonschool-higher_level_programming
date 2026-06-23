#!/usr/bin/env python3
"""
Task 3 - Develop a simple API using Python with http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("It serves different endpoints")
        """Handle GET requests for different endpoints"""

        # Root endpoint: /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data).encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # /info endpoint (optional per expected output)
        elif self.path == "/info":
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            response = json.dumps(info_data).encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response)
            return

        # Any undefined endpoint
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the server on port 8000"""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
