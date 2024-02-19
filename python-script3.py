import re

def extract_data_from_sql(file_path):
    with open(file_path, 'r') as file:
        sql_content = file.read()

    # Extract values within parentheses after VALUES keyword
    values_match = re.search(r'VALUES\s*\((.*?)\);', sql_content, re.DOTALL)

    if values_match:
        values_data = values_match.group(1)
        
        # Remove newlines and trim extra whitespaces
        values_data = re.sub(r'\s+', ' ', values_data).strip()

        # Separate each set of values by a comma
        values_list = re.findall(r'\([^)]*\)', values_data)

        # Join the values with a comma and newline
        result = ',\n'.join(values_list)

        return result

    else:
        return None

# Example usage:
file_path = 'insert_queries.sql'
result = extract_data_from_sql(file_path)

data_list = [item.strip() for item in result.split(',')]

# Join the strings with commas and enclose in square brackets
result_list = [f"{','.join(data_list[i:i+15])}" for i in range(0, len(data_list), 15)]

def transform_data(input_data):
    output = []
    for i in range(len(input_data)):
        
        # Use regular expression to find and replace the first two strings inside quotes
        new_string = re.sub(r'\(([^,]+),([^,]+)', r"('\1','\2'", input_data[i])

        output.append(new_string)
    return output


output_data = transform_data(result_list)
print(output_data)
# sql_file_path = 'output.sql'

# with open(sql_file_path, 'w') as sql_file:
#     sql_file.write("INSERT INTO Productivity (cidade, estado, jan, fev, mar, abr, mai, jun, jul, ago, set, out, nov, dez, anual)\nVALUES\n")

#     for data in output_data:
#         values = ', '.join(map(str, data))
#         sql_file.write(f"({values}),\n")

#     # Remove the trailing comma and newline from the last line
#     sql_file.seek(0, 2)  # Move to the end of the file
#     sql_file.seek(sql_file.tell() - 2, 0)  # Move back two characters
#     sql_file.truncate()  # Remove the comma and newline
#     sql_file.write(";")