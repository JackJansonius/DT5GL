


# Settings for connection to PosgreSQL database. 
# Name of database from the script via instruction PostgreSQL_database: "database name"
psql_host="localhost"           # "127.0.0.1"
psql_user="postgres1"
psql_password="******"
psql_port="5432"                # defaults to 5432 if it is not provided



# zerofill(1,2) => '01' ; str(1.5).zfill(4) => '01.5' (insert leading zeros)
def zerofill (number, length):
    return str(number).zfill(length)

# strcontains('ABCD', 'BC') => True
def strcontains(str1,str2):                          
    return str2 in str1



# functions for challenge: March-2024 Analyzing Employees #########################
# https://dmcommunity.org/challenge/challenge-march-2024/

import json

def read_json(file_path):
    global employees, selected_zip_codes
    with open(file_path, 'r') as file:
        data = json.load(file)
        employees = data['company']['employees']
        selected_zip_codes = data['company']['selectedZipCode']
    return 1

def len_employees():
    return len(employees)

def get_max_salary():
    salaries = [emp['salary'] for emp in employees]
    return max(salaries)

def employee_attribute (employee_nr, attribute):
    return employees[employee_nr][attribute]


import re

def sort_names_high_paid(data):
    # In: Name1(Integer1), Name2(Integer2), Name3(Integer3),... Out: sorted by descending integer value 
    entries = data.split(", ")
    sorted_entries = sorted(entries, key=lambda x: int(re.search(r'\((\d+)\)', x).group(1)), reverse=True)
    return (", ".join(sorted_entries))


# functions if no location decision table is used:
states = set()
def check_states (employee_nr):
    global states
    states = states | set(loc['state'] for loc in employees[employee_nr]['locations'])
    return 1

def get_states():
    return str(states)

employee_names_in_selected_zips = ""
def check_selected_zips(employee_nr):
    global employee_names_in_selected_zips
    for loc in employees[employee_nr]['locations']:
        if loc['zipCode'] in selected_zip_codes:
            employee_names_in_selected_zips += ", " + employees[employee_nr]['name'] + "(" + loc['zipCode'] + ")" 
            break
    return 1        

def get_employee_names_in_selected_zips():
    return "\n   " + employee_names_in_selected_zips[2:]       # skip initial ", "


# functions if a location decision table is used: 
def get_number_of_locations_for_employee(employee_nr):
    return len(employees[employee_nr]['locations'])

def get_selected_zip_codes(): 
    return str(selected_zip_codes)
    
def location_attribute(employee_nr, location_nr, attribute):
    return employees[employee_nr]['locations'][location_nr][attribute]

def newline():
    return "\n"

# END- functions for challenge: March-2024 Analyzing Employees #########################

# functions for challenge: April-2024 Using Lookup Tables in Decision Models ###### 
# https://dmcommunity.org/challenge/challenge-april-2024/


import csv

def load_json2(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def load_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def extract_claim(file_name):
    global procedures, diagnoses
    claim = load_json2(file_name)
    procedures = claim['claim']['procedures']
    diagnoses = claim['claim']['diagnoses']
    return 1

def extract_compatible_codes(file_name):
    global compatible_codes
    compatible_codes = load_csv(file_name)
    # Convert compatible codes to list of lists
    compatible_codes = [item for item in compatible_codes]    
    return 1

def extract_incompatible_codes(file_name):
    global incompatible_ranges
    incompatible_ranges = load_csv(file_name)           
    # Convert incompatible ranges to list of lists
    incompatible_ranges = [[item[0], item[1], item[2], item[3]] for item in incompatible_ranges]
    return 1

def len_procedures():
    return len(procedures)
    
def len_diagnoses():
    return len(diagnoses)
    
def get_procedure_type_from_claim(procedure_nr):
    return procedures[procedure_nr]["type"]

def get_procedure_code_from_claim(procedure_nr):
    return procedures[procedure_nr]["code"]

def get_diagnosis_code_from_claim(diagnosis_nr):
    return diagnoses[diagnosis_nr]["code"]

def CompatibleCodes(procedure_code, diagnose_code):
    return [diagnose_code, procedure_code] in compatible_codes 

def InCompatibleCodes(procedure_code, diagnose_code):   
    for range_item in incompatible_ranges:   
        if (range_item[0] <= procedure_code <= range_item[1]) and (range_item[2] <= diagnose_code <= range_item[3]):
            return True
    return False

# END- functions for challenge: April-2024 Using Lookup Tables in Decision Models ######












