import requests
import json

# My webpage
# Go the the link and press Ctrl + U to see the code and compare
response = requests.get('https://jasonpereira96.github.io/VDS-Assignment-1/')

print(response.text)




# ISRO centers data
# response = requests.get('https://isro.vercel.app/api/centres')

# print(print(json.dumps(json.loads(response.text), indent=4)))