import requests
import json
import sys

r = requests.post('https://6fyvhv2ao3.execute-api.us-east-1.amazonaws.com/dev1/buzz', json={'person':sys.argv[0]})
print(r.json())
