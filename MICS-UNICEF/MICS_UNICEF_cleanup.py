from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import  Font


wb = load_workbook("MICS_UNICEF_SurveyData.xlsx")
ws = wb.active

# Delete columns B(2), E(5), F(6), G(7)
ws.delete_cols(2)
ws.delete_cols(4, 3)

# Rename column titles for consistency
ws['A1'] = 'Title'
ws['B1'] = 'Country'
ws['C1'] = 'Start Year'
ws['D1'] = 'End Year'

# Format columns C1 (Start Year) and D1 (End Year) appropriately
for cell in ws['C']:
    currentCol = get_column_letter(cell.column) + str(cell.row)
    nextCol = get_column_letter(cell.column + 1) + str(cell.row)
    if "-" not in cell.value:
        ws[currentCol] = cell.value
        ws[nextCol] = cell.value

    # Cases with a range. e.g. 2011-2015 -> Start Year = 2011, End Year = 2015
    else:
        # Split range into two items. e.g. '2011-2015' -> ['2011', '2015']
        range = cell.value.split('-')
        ws[currentCol] = range[0]
        ws[nextCol] = range[1]

# Update 'Source' column
for cell in ws['D']:
    nextCol = get_column_letter(cell.column + 1) + str(cell.row)
    ws[nextCol] = 'MICS_UNICEF'
ws['E1'] = 'Source'

# Save changes to a new file
wb.save("MICS_UNICEF_cleaned.xlsx")
