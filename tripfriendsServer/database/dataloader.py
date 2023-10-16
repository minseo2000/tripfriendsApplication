import openpyxl

def showFileContents(file_name='./unknown_area/unknown_place_list.xlsx', sheet_name="전체"):
    # Open the Excel file

    workbook = openpyxl.load_workbook(file_name)

    # Select a sheet within the workbook
    sheet = workbook[sheet_name]

    # Read the data
    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            print(cell)
        print()
    # Close the workbook
    workbook.close()


showFileContents()