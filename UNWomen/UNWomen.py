import requests

url_unwomen = 'https://evaw-global-database.unwomen.org/VAW/ExportToExcellDataList?countryId=&urlstring=https://evaw-global-database.unwomen.org/en/search'

# Download UNWomen
req = requests.get(url_unwomen)
url_content = req.content
csv_file = open('UNWomen_SurveyData.csv', 'wb')

csv_file.write(url_content)
csv_file.close()
