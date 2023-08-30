import openpyxl
import sys

def delete_row(source_file):
        # Load the workbook
        workbook = openpyxl.load_workbook(source_file)
    
        # Select the desired sheet
        sheet = workbook.active
    
        #Delete first row of spreadsheet
        sheet.delete_rows(1,1)
    
        #Save workbook
        workbook.save(source_file)
        
        print("delet_first_row ran successfully")
        
if len(sys.argv) == 2:
    source_file = sys.argv[1]
    delete_row(source_file)