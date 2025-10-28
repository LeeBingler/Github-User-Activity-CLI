#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests


def parser():
    if len(sys.argv) != 2:
        return -1
    else:
        return 0

def fetchData():
    response = requests.get(f"https://api.github.com/users/{sys.argv[1]}/events")

    if response.status_code != 200:
        return response.status_code

    return response

def main():
    if parser() != 0:
        print("Wrong argument")
        return -1

    data = fetchData()

    if type(data) == int:
        print(f"Error in fetching data: {data}")
        return -1

    return 0
    


if __name__ == "__main__":
    main()