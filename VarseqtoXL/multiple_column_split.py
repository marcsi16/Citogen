import pandas as pd
import sys

def split_columns_by_headers(source_file, column_mappings):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(source_file)
  
    for mapping in column_mappings:
        header_name = mapping['header_name']
        separator = mapping['separator']
        new_col_names = mapping['new_col_names']

        # Split the column using the separator and expand it into new columns
        split_data = df[header_name].str.split(separator, expand=True)
        split_data.columns = new_col_names
        
        # Concatenate the split columns to the original DataFrame
        df = pd.concat([df, split_data], axis=1)
    
    # Save the DataFrame back to the Excel file
    df.to_excel(source_file, index=False)
   
if len(sys.argv) == 2:
    source_file = sys.argv[1]
    
    # Specify the column mappings for each column you want to split
    column_mappings = [
        {
            'header_name': 'Chr:Pos',
            'separator': ':',
            'new_col_names': ['Chr', 'Pos']
        },
        {
            'header_name': 'Ref/Alt',
            'separator': '/',
            'new_col_names': ['Ref', 'Alt']
        },
        {
            'header_name': 'HGVS c. (Clinically Relevant)',
            'separator': ':',
            'new_col_names': ['NM', 'c.DNA']
        },
        {
            'header_name': 'HGVS p. (Clinically Relevant)',
            'separator': ':',
            'new_col_names': ['NP', 'protein']
        },
        # Add more mappings for additional columns
    ]
    
    # Call the function to split the specified columns and save the changes in the same file
    split_columns_by_headers(source_file, column_mappings)
    
    print("multiple_column_split ran successfully")