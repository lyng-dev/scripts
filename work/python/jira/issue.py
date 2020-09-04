from jira import JIRA
import os
import json
import sys
from enum import Enum

print('creating new issue')
username =os.getenv('jira_username', 'invalid_user')
server   =os.getenv('jira_server', '')
password =os.getenv('jira_apikey', 'invalid_key')


options={'server': server}

jira=JIRA(options, basic_auth=(username, password))

new_issue=jira.create_issue(project='ALFA',summary=sys.argv[1], description=sys.argv[2], issuetype={'name': 'Issue'})
