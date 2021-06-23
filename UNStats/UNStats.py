import requests

url_unstatswomen = 'https://public.tableau.com/vizql/w/TimeUse_DRAFT/v/DATADOWNLOAD-WOMEN/vudcsv/sessions/E96BA7EC1C5E47FA9AFBC716433FE9CB-0:0/views/7713620505763405234_16317244867269036255?underlying_table_id=Migrated%20Data&underlying_table_caption=Full%20Data'
url_unstatsmen = 'https://public.tableau.com/vizql/w/TimeUse_DRAFT/v/DATADOWNLOAD-MEN/vudcsv/sessions/E96BA7EC1C5E47FA9AFBC716433FE9CB-0:0/views/7713620505763405234_15010888941265086071?underlying_table_id=Migrated%20Data&underlying_table_caption=Full%20Data'

# Download UNStats (Women)
req = requests.get(url_unstatswomen)
url_content = req.content
csv_file = open('UNStatsWomen_SurveyData.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

# Download UNStats (Men)
req = requests.get(url_unstatsmen)
url_content = req.content
csv_file = open('UNStatsMen_SurveyData.csv', 'wb')

csv_file.write(url_content)
csv_file.close()
