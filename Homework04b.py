"""
Created on Feb 13 17:50:15 2018

@author: Pan Chen
"""
import requests
import json


def get_user_repositories(user_id):
    url = 'https://api.github.com/users/' + user_id + '/repos'
    response = json.loads(requests.get(url).text)
    rt = []
    for i in response:
        rt.append(i['name'])
    return rt


def get_commits(user_id, repository):
    url = 'https://api.github.com/repos/' + user_id + '/' + repository + '/commits'
    response = json.loads(requests.get(url).text)
    return len(response)


def get_commits_numbers(user_id):
    repositories = get_user_repositories(user_id)
    commits_number = {}
    for repository in repositories:
        commits_number[repository] = get_commits(user_id, repository)
    return commits_number


def print_info(user_id):
    dic = get_commits_numbers(user_id)
    print('User: ' + user_id)
    for repository in dic:
        print('Repo: ' + repository + " Number of commits: " + str(dic[repository]))


if __name__ == '__main__':
    user_id = "pchen12567"
    print_info(user_id)
