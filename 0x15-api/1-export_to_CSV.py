#!/usr/bin/python3
"""Exports employee To Do List to .csv"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Obtain url and user_id
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Build apis
    user = requests.get(url + f"users/{id}").json()
    username = user.get(f"username")
    todos = requests.get(url + f"todos", params={f"userId": id}).json()

    # Write apis to csv file
    with open(f"{id}.csv", f"w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id, username, t.get(f"completed"), t.get(f"title")]
         ) for t in todos]
