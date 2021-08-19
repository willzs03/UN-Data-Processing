import json
import requests
import pandas as pd
from pandas import json_normalize

# Read in the Survey Data file downloaded from ILO's website. This will be used to retrieve the unique IDs within ILO
df = pd.read_csv("ILO_SurveyData.csv")

# Initialize empty containers
ids = []
metadata = []

# Loop through every item/entry in the .csv file, retrieve the unique ID, and store it within a list
for item in df["id"]:
    ids.append(item)

# For debugging purposes
counter = 0

# Initialize a new pandas frame
frame = pd.DataFrame()

# Test run with a random unique ID
# Metadata URL https://www.ilo.org/surveyLib/index.php/api/catalog/find_by_id/{id}
# test = requests.get('https://www.ilo.org/surveyLib/index.php/api/catalog/find_by_id/' + str(1000))
# if test.status_code != 404:
#     test = json.loads(test.text)
#     test = json_normalize(test)
#     test = test.reset_index(drop=True)
#     frame = pd.concat([frame, test], axis=0)

# Loop through every ID, pull up their respective metadata information, and append the metadata information
for item in ids:
    test = requests.get('https://www.ilo.org/surveyLib/index.php/api/catalog/find_by_id/' + str(item))
    if test.status_code != 404:
        test = json.loads(test.text)
        test = json_normalize(test)
        test = test.reset_index(drop=True)
        frame = pd.concat([frame, test], axis=0)
    print(counter)
    counter += 1

# Save all retrieved metadata information into an excel file
frame.to_excel("ILO_Metadata.xlsx", index=False)


