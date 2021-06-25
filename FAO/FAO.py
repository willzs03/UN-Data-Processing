import requests

url = 'https://microdata.fao.org/index.php/catalog/export/csv?ps=5000&collection[]='
r = requests.get(url, allow_redirects=True)

# Check what format the file is in (e.g. .csv or .xlsx)
# print(r.headers.get('content-type'))

open('FAO_SurveyData.csv', 'wb').write(r.content)
