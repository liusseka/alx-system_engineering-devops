#!/usr/bin/python3

"""Returns To DO List info for an employee"""

import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + f"users/{sys.argv[1]}").json()
    to_dos = requests.get(url + f"todos",
        params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in to_dos if t.get("completed") is True]
    print(f"Employee {employee.get("name")}"
        f"is done with tasks({len(completed)}/{len(to_dos)}):")

    [print("\t {}".format(c)) for c in completed]
