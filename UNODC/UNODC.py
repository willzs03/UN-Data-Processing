import requests

url = 'https://www.cdeunodc.inegi.org.mx/unodc/wp-content/uploads/2020/12/Diccionario_datos_victimi_2016_2019.xlsx'
r = requests.get(url, allow_redirects=True)

# Check what format the file is in (e.g. .csv or .xlsx)
# print(r.headers.get('content-type'))

open('UNODC_surveyData.xlsx', 'wb').write(r.content)
