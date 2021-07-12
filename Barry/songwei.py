# Load the required library
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import re

# Read csv
fao = pd.read_csv('FAO_SurveyData.csv')
ihsn = pd.read_csv('IHSN_SurveyData.csv')
ilo = pd.read_csv('ILO_SurveyData.csv')
un_population = pd.read_csv('UNPopulation_SurveyData.csv')

# FAO
fao.head()
fao['source'] = 'FAO'
fao_new = fao[['nation', 'title', 'year_start', 'year_end', 'source']]
fao_new['year_start'] = fao_new['year_start'].replace(0, np.nan)
fao_new['year_end'] = fao_new['year_end'].replace(0, np.nan)
fao_new.head()
fao_new.shape

# IHSN
ihsn['source']='IHSN'
ihsn_new = ihsn[['nation', 'title', 'year_start', 'year_end', 'source']]
ihsn_new['year_start'] = ihsn_new['year_start'].replace(0, np.nan)
ihsn_new['year_end'] = ihsn_new['year_end'].replace(0, np.nan)
ihsn_new.head()
ihsn_new.shape

# ILO
ilo['source']='ILO'
ilo_new = ilo[['nation', 'title', 'year_start', 'year_end', 'source']]
ilo_new['year_start'] = ilo_new['year_start'].replace(0, np.nan)
ilo_new['year_end'] = ilo_new['year_end'].replace(0, np.nan)
ilo_new.head()

# UN POPULATION
un_population['source']='UN Population'

# Extract start and end year
un_population['year'] = un_population['Catalog'].str.extract("(\d*\-*\d+)", expand=True)
un_population['start_year'] = un_population['year'].str[:4]
un_population['end_year'] = un_population['year'].str.extract('\-(\d{4}\s*$)', expand=True)
un_population['end_year'].fillna(un_population['start_year'], inplace=True)

# Rename columns in UN Population
un_new = un_population[['Location', 'Catalog', 'start_year', 'end_year', 'source']]
un_new = un_new.rename(columns={'Location': 'nation', 'Catalog': 'title', 'start_year':'year_start', 'end_year':'year_end', 'source':'source'})
un_new.head()

# Merge data sets
merge = pd.concat([fao_new, ihsn_new, ilo_new, un_new])
merge.head(20)

# ouput csv
merge.to_excel('merge_data.xlsx',index=False)


