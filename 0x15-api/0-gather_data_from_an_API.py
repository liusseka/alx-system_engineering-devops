#!/usr/bin/python3

"""Returns To DO List info for an employee"""

import requests
import sys

if __name__ == "__main__":
    # Obtain url
    url = f"https://jsonplaceholder.typicode.com/"

    # build Api
    employee = requests.get(url + f"users/{sys.argv[1]}").json()
    id = sys.argv[1]
    to_dos = requests.get(url + f"todos", params={"userId": id}).json()

    # Get todo data
    completed = [t.get("title") for t in to_dos if t.get("completed") is True]
    name = employee.get('name')
    num_comps = len(completed)
    num_rems = len(to_dos)
    
    # print todo data
    print(f"Employee {name} is done with tasks({num_comps}/{num_rems}):")

    [print("\t {}".format(c)) for c in completed]
