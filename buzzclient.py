#!/usr/bin/env python3

import requests
import json
import sys

r = requests.post('https://6fyvhv2ao3.execute-api.us-east-1.amazonaws.com/dev1/buzz', json={'person':sys.argv[1]})
print(r.json())
