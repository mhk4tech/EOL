# Mock data to stimulate a queryset result
mock_data = [
{
    'SSN': '000000001',
    'Name': 'test name 1',
    'Type': '1'
},
{
    'SSN': '000000002',
    'Name': 'test name 2',
    'Type': '4'
},
{
    'SSN': '000000003',
    'Name': 'test name 3',
    'Type': '1'
},
{
    'SSN': '000000004',
    'Name': 'test name 4',
    'Type': '3'
},
{
    'SSN': '000000005',
    'Name': 'test name 5',
    'Type': '6'
},
{
    'SSN': '000000006',
    'Name': 'test name 6',
    'Type': '3'
}
]

import csv

RESTRICTED_EMP_TYPE_LST = [1,3] # List all the restircted employee type here.

with open('EOL.csv', 'w') as new_file: # Create and open a new csv file 'EOL.csv'
    fieldnames = ['SSN', 'Name', 'Type']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    for data in mock_data: # Fetch data from query set result (mock data here).
        if int(data['Type']) in RESTRICTED_EMP_TYPE_LST: # Check for restiricted employee type
            csv_writer.writerow(data) # Add row to csv file.

"""Final EOL.csv file output

SSN,Name,Type
000000001,test name 1,1
000000003,test name 3,1
000000004,test name 4,3
000000006,test name 6,3

"""






