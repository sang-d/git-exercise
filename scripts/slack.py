# API slackClient v1: https://github.com/slackapi/python-slackclient/tree/v1
# API slackClient 2: https://slack.dev/python-slackclient/conversations.html#direct-messages

import slack
import os
print("start slack script")
token = os.environ.get('slack_token')
admin_user_id = os.environ.get('admin_user_id')
client = slack.WebClient(token=token)


# client.conversations_open(users=[myid])
# response = client.chat_postMessage( channel='DF7MJ83EE', text="",as_user=True)

# users = client.api_call("users.list")
# mm = users.get("members")
# for m in mm:
# 	if m.get("profile").get("email") == "sang.dinh@wizeline.com":
# 		print(m)


# uinfo = client.api_call("users.info")

# uu = client.api_call("users.lookupByEmail")