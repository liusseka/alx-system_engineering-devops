#!/usr/bin/python3
"""Exports employee To Do List to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    # take argument and url
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # build apis
    user = requests.get(url + f"users/{id}").json()
    username = user.get(f"username")
    to_dos = requests.get(url + "todos", params={"userId": id}).json()

    # create json file
    with open(f"{id}.json", "w") as jsonfile:
        json.dump({id: [{
                "task": t.get(f"title"),
                "completed": t.get(f"completed"),
                "username": username
        } for t in to_dos]}, jsonfile)
