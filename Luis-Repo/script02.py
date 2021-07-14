import json
import requests
import pandas as pd
from pandas import json_normalize

with open("catalog.json") as data_file:
    catalog = json.load(data_file)

n = len(catalog)

#print(catalog[0])
frame = pd.DataFrame()
for idx, s in enumerate(catalog):
    uniqueid = s['id']
    if uniqueid == 8478:
        pass
    else:
        i = requests.get('http://catalog.ihsn.org/metadata/export/' + str(uniqueid) + '/json')
        i = json.loads(i.text)
        i = json_normalize(i)
        i = i.reset_index(drop=True)

        if s == 0:
            frame = i
        else:
            frame = pd.concat([frame, i], axis=0)
        print(f'Processed {idx} out of {n}')

frame.to_excel("output.xlsx")