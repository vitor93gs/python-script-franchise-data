import re

#TRANSFORMAÇÃO DAS QUERIES EM  LISTA DE STRINGS

data_string = "(ACRELÂNDIA,AC,4521,4522,4247,4371,3960,4084,4284,4807,4915,5008,4885,4574,4515), (ASSIS BRASIL,AC,4678,4661,4231,4532,3917,4026,4283,4947,5136,5092,5102,4771,4615), (BRASILÉIA,AC,4655,4653,4268,4566,3945,4079,4285,4858,5102,5105,5157,4771,4620), (BUJARI,AC,4501,4621,4231,4401,4011,4111,4316,4885,5031,5131,4989,4580,4567), (CAPIXABA,AC,4486,4527,4264,4395,3957,3983,4228,4823,5070,5138,4952,4677,4542), (CRUZEIRO DO SUL,AC,4738,4902,4248,4455,4285,4164,4363,4996,5135,5024,4950,4701,4663)"

# Remove unnecessary characters and split into individual strings
data_list = [item.strip() for item in data_string.split(',')]

# Join the strings with commas and enclose in square brackets
result_list = [f"{','.join(data_list[i:i+15])}" for i in range(0, len(data_list), 15)]

print(result_list)

def transform_data(input_data):
    output = []
    for i in range(len(input_data)):
        
        # Use regular expression to find and replace the first two strings inside quotes
        new_string = re.sub(r'\(([^,]+),([^,]+)', r"('\1','\2'", input_data[i])

        output.append(new_string)
    return output

# Example usage
input_data = ['(ACRELÂNDIA,AC,4521,4522,4247,4371,3960,4084,4284,4807,4915,5008,4885,4574,4515)', '(ASSIS BRASIL,AC,4678,4661,4231,4532,3917,4026,4283,4947,5136,5092,5102,4771,4615)']
output_data = transform_data(input_data)
print(output_data)
