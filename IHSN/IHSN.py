import requests

url_ihsn = 'http://catalog.ihsn.org/catalog/export/csv?ps=10000&collection[]=central'

# Download IHSN
req = requests.get(url_ihsn)
url_content = req.content
csv_file = open('IHSN_SurveyData.csv', 'wb')

csv_file.write(url_content)
csv_file.close()
