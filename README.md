# Auto Invite To Org By Issue Comment

A GitHub action script to automatically invite everyone to the organization who comment at the issue page.

## What is this?

START, FORK this.

Next You can write `.invite me` at [here](https://github.com/BaseMax/AutoInviteToOrgByIssueComment/issues/1
), after that you will be invited to a surprising and fantastic organization.

----------

## Deploy to your organization

#### Create `MY_GITHUB_KEY` variable at Secrets

Open https://github.com/settings/tokens and create one.

After that you can create a secret at `https://github.com/ORG_NAME/REPO_NAME/settings/secrets/actions`.

#### Create `COMMUNITY_TEAM_ID` variable at Secrets

At first, create a team at `https://github.com/orgs/YOUR_ORG_NAME/teams` and run:


```
curl -H "Authorization: token *****" https://api.github.com/orgs/YOUR_ORG_NAME/teams
```

p.s: Put your personal token at the `****`, and replace your organization name at `YOUR_ORG_NAME`.

After that you can create a secret at `https://github.com/ORG_NAME/REPO_NAME/settings/secrets/actions` and put api number as value.

#### Create `.github/workflows/invite-by-comment.yml` file:

```yaml
on:
  issue_comment:
    types: [created, edited]
name: Invite a new user by comment
jobs:
    build:
      runs-on: ubuntu-latest

      steps:
        - name: checkout repo content
          uses: actions/checkout@v2
        - name: setup python
          uses: actions/setup-python@v2
          with:
            python-version: 3.8
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install requests
            if [ -f ./.github/workflows/requirements.txt ]; then pip install -r ./.github/workflows/requirements.txt; fi
        - name: execute py script
          run: |
            python ./.github/workflows/AutoInviteToOrgByIssueComment.py
          env:
            MY_GITHUB_KEY: ${{ secrets.MY_GITHUB_KEY }}
            COMMUNITY_TEAM_ID: ${{ secrets.COMMUNITY_TEAM_ID }}
```

### Create `.github/workflows/AutoInviteToOrgByIssueComment.py` file

```python
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

  if ".invite @" in COMMENT
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
```

© Copyright Max Base, 2021
