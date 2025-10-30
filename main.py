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

    if response.ok == False:
        return response.status_code

    return response

class bcolors:
    TYPE = "\033[95m"
    DATE = "\033[94m"
    NAME = "\033[93m"
    END = "\033[0m"

def _handleType(type):
    match type:
            case "CreateEvent":
                print(bcolors.TYPE + "Created " + bcolors.END, end='')
            case "DeleteEvent":
                print(bcolors.TYPE + "Deleted " + bcolors.END, end='')
            case "DiscussionEvent":
                print(bcolors.TYPE + "Created discussion in " + bcolors.END, end='')
            case "GollumEvent":
                print(bcolors.TYPE + "Created/Update a wiki page in " + bcolors.END, end='')
            case "IssueCommentEvent":
                print(bcolors.TYPE + "Interacted with an issue discussion in " + bcolors.END, end='')
            case "MemberEvent":
                print(bcolors.TYPE + "Interacted with " + bcolors.END, end='')
            case "PublicEvent":
                print(bcolors.TYPE + "Maded public " + bcolors.END, end='')
            case "PullRequestEvent":
                print(bcolors.TYPE + "Interacted with pull request of " + bcolors.END, end='')
            case "PullRequestReviewEvent":
                print(bcolors.TYPE + "Interacted with pull request review of " + bcolors.END, end='')
            case "PullRequestReviewCommentEvent":
                print(bcolors.TYPE + "Interacted with pull request review comment of " + bcolors.END, end='')
            case "PushEvent":
                print(bcolors.TYPE + "Pushed a commit in " + bcolors.END, end='')
            case "ReleaseEvent":
                print(bcolors.TYPE + "Interacted with release of " + bcolors.END, end='')
            case "WatchEvent":
                print(bcolors.TYPE + "Stars " + bcolors.END, end='')
            case _:
                print("ERROR", type)

def formatString(output):
    print(bcolors.DATE + f"[{output["created_at"]}]" + bcolors.END, end=" ")
    
    _handleType(output["type"])
    
    print(bcolors.NAME + output["repo"]["name"] + bcolors.END)

def main():
    if parser() != 0:
        print("Wrong argument")
        return -1

    data = fetchData()

    if type(data) == int:
        print(f"Error in fetching data: {data}")
        return -2

    json = data.json()

    for output in json:
        formatString(output)

    return 0
    


if __name__ == "__main__":
    main()