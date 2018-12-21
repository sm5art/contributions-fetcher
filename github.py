import json
import requests

def get_oauth():
    with open('oauth.txt', 'r') as f:
        return f.read().strip()

def get_repos(user):
    url = "https://api.github.com/users/%s/repos?access_token=%s" % (user, get_oauth())
    req =  requests.get(url)
    return json.loads(req.text)
