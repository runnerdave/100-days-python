from datetime import datetime
import os
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PIXELA_URL = "https://pixe.la/v1/users"
TOKEN = "19F45C72-2F66-4A83-BE1A-6644F3E24ED0"
USERNAME = "runnerdave"
GRAPH_ID = "graph1"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# one off user creation
# response = requests.post(url=url, json=params, verify=False)
# response.raise_for_status()
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@runnerdave , it is your profile page!","isSuccess":true}

graph_endpoint = f"{PIXELA_URL}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create the graph
# response = requests.post(url=graph_endpoint, verify=False, json=graph_config, headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}
# graph created: https://pixe.la/v1/users/runnerdave/graphs/graph1.html

# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

graph_url = f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
graph_data = {
    "date":today_formatted,
    "quantity":"3.3"
}

# add to the graph
# response = requests.post(url=graph_url, verify=False, json=graph_data, headers=headers)
# print(response.text)

# update example
# PUT - /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

update_graph_url = f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"
graph_data = {
    "quantity":"25",
}
# response = requests.put(url=update_graph_url, verify=False, json=graph_data, headers=headers)
# print(response.text)

# delete example
#  /v1/users/<username>/graphs/<graphID>
delete_graph_url = f"{PIXELA_URL}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.delete(url=delete_graph_url, verify=False, headers=headers)
print(response.text)