#!/usr/bin/python3
"""Exports to-do list to JSON format."""
import json
import requests

if __name__ == "__main__":
    # Obtain url and users
    url = f"https://jsonplaceholder.typicode.com/"
    users = requests.get(url + f"users").json()

    # Write data to jdon file
    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get(f"id"): [{
                "task": t.get(f"title"),
                "completed": t.get(f"completed"),
                "username": u.get(f"username")
            } for t in requests.get(url + f"todos",
                                    params={"userId": u.get(f"id")}).json()]
            for u in users}, jsonfile)
