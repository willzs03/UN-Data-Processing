import json
import requests
import math

test = requests.get('http://catalog.ihsn.org/metadata/export/8478/json')
if test.status_code == 404:
    print("404 error")
else:
    print(test.status_code)

