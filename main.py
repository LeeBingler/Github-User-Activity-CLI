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

def formatString(output):
    print(f"[{output["created_at"]}]", end=" ")
    
    type = output["type"]

    match type:
        case "CreateEvent":
            print("Created ", end='')
        case "DeleteEvent":
            print("Deleted ", end='')
        case "DiscussionEvent":
            print("Created discussion in ", end='')
        case "GollumEvent":
            print("Created/Update a wiki page in ", end='')
        case "IssueCommentEvent":
            print("Interacted with an issue discussion in ", end='')
        case "MemberEvent":
            print("Interacted with ", end='')
        case "PublicEvent":
            print("Maded public ", end='')
        case "PullRequestEvent":
            print("Interacted with pull request of ", end='')
        case "PullRequestReviewEvent":
            print("Interacted with pull request review of ", end='')
        case "PullRequestReviewCommentEvent":
            print("Interacted with pull request review comment of ", end='')
        case "PushEvent":
            print("Pushed a commit in ", end='')
        case "ReleaseEvent":
            print("Interacted with release of ", end='')
        case "WatchEvent":
            print("Stars ", end='')
        case _:
            print("ERROR", type)
    
    print(output["repo"]["name"])

def main():
    if parser() != 0:
        print("Wrong argument")
        return -1

    data = fetchData()

    if type(data) == int:
        print(f"Error in fetching data: {data}")
        return -1

    json = data.json()

    for output in json:
        formatString(output)

    return 0
    


if __name__ == "__main__":
    main()