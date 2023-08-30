#Master script calling other py modules
import openpyxl
import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import subprocess

def varseq_to_xl(source_file, destination_file):
    
    #Delete first row
    subprocess.run(["python","delete_first_row.py", source_file])
    
    #Split columns that have 2 data parts
    subprocess.run(["python", "multiple_column_split.py", source_file])
    
    # Add data: sample number, date
    subprocess.run(["python", "add_part_of_filename_to_sheet.py", source_file])
    subprocess.run(["python", "add_date.py", source_file])
    
    #Copy data from source to destination by headers
    subprocess.run(["python", "data_copy_by_headers.py", source_file, destination_file])
    
    #Format copied data in destination spreadsheet
    subprocess.run(["python", "format.py", source_file, destination_file])

#if __name__ == "__main__":
#    source_file = "C:/Users/ACER/Documents/Citogenetika/Python/Source - 87230-PC.xlsx"
 #   destination_file = "C:/Users/ACER/Documents/Citogenetika/Python/Target.xlsx"
  #  varseq_to_xl(source_file, destination_file)
   # print("Data copied.")
    
    
if __name__ == "__main__":
    source_file = input("Enter the source Excel file name: ")
    destination_file = input("Enter the destination Excel file name: ")
    varseq_to_xl(source_file, destination_file)
    print("Data copied.")