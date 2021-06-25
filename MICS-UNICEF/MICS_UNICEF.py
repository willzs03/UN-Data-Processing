import requests

url = 'https://mics.unicef.org/api/surveysCatalogue'
r = requests.get(url, allow_redirects=True)

# Check what format the file is in (e.g. .csv or .xlsx)
# print(r.headers.get('content-type'))

open('MICS_UNICEF_SurveyData.csv', 'wb').write(r.content)
