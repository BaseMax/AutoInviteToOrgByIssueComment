# Max Base
# 2021-06-19
# https://github.com/BaseMax/AutoInviteToOrgByIssueComment

import os
import sys
import json
import requests

print("Hello, World")

if os.getenv('CI'):
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')

print("Environ:")
print(os.environ)
print("Prefix:")
print(sys.prefix)

MY_GITHUB_KEY = os.environ['MY_GITHUB_KEY']
COMMUNITY_TEAM_ID = os.environ['COMMUNITY_TEAM_ID']

file = open(os.environ['GITHUB_EVENT_PATH'])
data = json.load(file)

print("Data:")
print(data)

COMMENT = data["comment"]["body"]
USERNAME = data["comment"]["user"]["login"]

if ".invite @" not in COMMENT and ".invite me" not in COMMENT:
  sys.exit()
else:

  if ".invite @" in COMMENT:
    USERNAME = COMMENT.replace(".invite @", "")

  print('Send invite for the @'+USERNAME)

  # TODO: check user already joined or no....
  url = 'https://api.github.com/teams/'+COMMUNITY_TEAM_ID+'/memberships/' + USERNAME
  payload=''
  headers = {
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': 'token '+MY_GITHUB_KEY
  }
  response = requests.request("PUT", url, headers=headers, data=payload)
  print(response.text)
