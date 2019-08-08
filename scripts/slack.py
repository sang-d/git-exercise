# API slackClient v1: https://github.com/slackapi/python-slackclient/tree/v1
# API slackClient 2: https://slack.dev/python-slackclient/conversations.html#direct-messages

import os
import sys
from slackclient import SlackClient

# print("start slack script")
token = os.environ.get('slack_token')
admin_user_id = os.environ.get('admin_user_id')

sc = SlackClient(token)

# res = sc.api_call(  "chat.postMessage", channel=admin_user_id, text="Hi", as_user=True)
email = sys.argv[1]
print('email', email)
if not email:
	res = sc.api_call(  "chat.postMessage", channel=admin_user_id, text="Couldn't find email", as_user=True)
else:
	response = sc.api_call("users.lookupByEmail", email=email)
	
user = response.get('user')
print(user.get('id'), user.get('name'))
