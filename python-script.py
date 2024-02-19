import pandas as pd
import re

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv', delimiter='\t')

# Update the SQL query template with correct column names
sql_query_template = """
({xpd}),"""
sql_query_template_final = """
({xpd});"""


# Open a file to write the SQL queries
with open('insert_queries.sql', 'w' ,encoding='utf-8') as f:
    f.write("""INSERT INTO Productivity (cidade, estado, jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez, anual)
VALUES """)
    # Iterate through DataFrame rows and write queries to the file
   
    for index, row in df.iterrows():
        # Format the query with row data
        data = {
            'xpd' : row.to_dict()['CIDADE,ESTADO,JAN,FEV,MAR,ABR,MAI,JUN,JUL,AGO,SET,OUT,NOV,DEZ,ANUAL']
        }
        query = sql_query_template.format(**data)
        
        new_string_with_double_quotes = query.replace("'","''")
        new_string = re.sub(r'\(([^,]+),([^,]+)', r"('\1','\2'", new_string_with_double_quotes)
            
        # Write the query to the file
        if index == df.size-1:
            final_string_with_double_quotes = sql_query_template_final.format(**data).replace("'","''")
            final_string = re.sub(r'\(([^,]+),([^,]+)', r"('\1','\2'", final_string_with_double_quotes)
            f.write(final_string)
        else:
            f.write(new_string)

print("SQL queries generated and saved to insert_queries.sql")
