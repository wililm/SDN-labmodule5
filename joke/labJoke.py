#!/usr/bin/python3

import requests

URL = "https://api.icndb.com/jokes/random"

payload ={}
headers = {'Accept': 'application/json'}
response = requests.get(URL, headers=headers, data=payload)
responseJSON = response.json()
joke = responseJSON['value']['joke']
print(joke)
