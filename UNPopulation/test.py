import pandas

sheet = pandas.read_excel('UNPopulation_SurveyData.xlsx')

sheet.loc[:,"Type"]

sheet.to_excel('test.xlsx', index=False)