import json
import requests
import math

test = requests.get("http://catalog.ihsn.org/api/catalog/search?year_start>1990&ps=1&page=1")
test = json.loads(test.text)

n = test['result']['found']

page_size = 100

pages = math.ceil(n/page_size)

print(pages)

print(range(pages))

catalog = []

for p in range(pages):
    test = requests.get('http://catalog.ihsn.org/api/catalog/search?year_start>1990&ps='+ str(page_size) +'&page=' + str(p+1))
    test = json.loads(test.text)

    catalog.extend(test['result']['rows'])
    print(f'Processing page {p}')

# Write filtered TODOs to file.
with open("data/catalog.json", "w") as data_file:
    json.dump(catalog, data_file, indent=2)

metadata = []
for s in catalog:
    id = s['id']
    test = requests.get('http://catalog.ihsn.org/metadata/export/'+str(id)+'/json')
    test = json.loads(test.text)

    metadata.append(test)


# Write filtered TODOs to file.
with open("data/metadata.json", "w") as data_file:
    json.dump(metadata, data_file, indent=2)
