# Exercise 6, string formatting and regular expressions
import re

infile = open ('postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid   = 0
invalid = 0

valid_districts_lines = open('validpc.txt').readlines()

valid_districts = {}
for valid_districts_line in valid_districts_lines:
    validpcs_line = valid_districts_line.strip()
    area, country = valid_districts_line.split(',')
    valid_districts[area] = country



for postcode in infile:
    # Ignore empty lines
    if postcode.isspace(): continue
    
    # Remove newlines, tabs and spaces
    postcode = re.sub(r"\s", "", postcode)
    
    # Convert to uppercase
    postcode = postcode.upper()  
    

    # Insert a space before the final digit and 2 letters
    postcode = re.sub(r'(.{3})$', r' \1', postcode)
    
    # Print the reformatted postcode
    print (postcode)

    #  Validate the postcode, returning a match object 'm'
    m = re.match(r'^([A-Z]{1,2}\d{1,2}[A-Z]?) [0-9]{1,2}[A-Z]{2}$', postcode)

    if m:
        
        district = m.group(1)
        if not district in valid_districts:
            print(f'District {district} is not valid!')
        
        valid   = valid + 1
        
    else:
        invalid = invalid + 1
        

infile.close()

print(f'Valid = {valid}')
print(f'Invalid = {invalid}')