#!/usr/bin/env python3
"""
Task 2 - Consuming and processing data from an API using Python
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print status + titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # Check success
    if response.status_code == 200:
        posts = response.json()  # parse JSON

        # Print each title
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them as posts.csv (id, title, body)"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # extract only id, title, body
        cleaned_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(cleaned_posts)
