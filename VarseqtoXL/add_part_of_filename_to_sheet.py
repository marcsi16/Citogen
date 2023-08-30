import pandas as pd
import sys

if len(sys.argv) == 2:
    source_file = sys.argv[1]
    
    # Load the Excel file into a DataFrame
    df = pd.read_excel(source_file)

    # Extract multiple parts of the filename
    file_parts = source_file.split(' - ')  # Modify this according to your filename structure
    part1 = file_parts[0]  # Extract the second part
    part2 = file_parts[1]

    # Split the third part using a different character
    part3 = file_parts[1].split('-')[0]  # Remove the file extension

    # Add the extracted parts as new columns
    df['Mintaszam'] = part3

    # Write the updated DataFrame back to the same Excel file
    df.to_excel(source_file, index=False)
      
    print("add_part_of_filename_to_sheet ran successfully")