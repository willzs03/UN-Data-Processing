# https://stackoverflow.com/questions/15793349/how-to-concatenate-three-excels-files-xlsx-using-python
import pandas as pd

# filenames
excel_names = ["IHSN_FAO_ILO_cleaned.xlsx", "MICS_UNICEF_cleaned.xlsx", "UNODC_cleaned.xlsx", "UNWomen_cleaned.xlsx"]

# read them in
excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)

# write it out
combined.to_excel("master.xlsx", header=False, index=False)