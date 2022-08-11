import csv

from sqlalchemy.engine import create_engine

RESTRICTED_EMP_TYPE_LST = [1,3] # List all the restircted employee type here.

engine = create_engine('mysql://<UserName>:<DBPassword>@<Database Host>/<Database Name>') # Sample: 'mysql://root:pass@172.17.0.2:3306/classicmodels'

conn = engine.connect()

result = conn.execute("""
    <QueryStatement>
""") # Sample: SELECT * FROM customers;

rows = result.fetchall() # rows sample: [(1, u'Kenial', u'Lee', u'SE'), (2, u'Jon', u'Skeet', u'Author')]
# Need to know the postion of each cloumn. Eg. "(1, u'Kenial', u'Lee', u'SE')"" represent a single row. 
# row[0] will be '1', row[2] will be 'Kenial' and row[3] will be 'SE'
with open('EOL.csv', 'w') as new_file: # Create and open a new csv file 'EOL.csv'
    fieldnames = ['SSN', 'Name', 'Type']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

    csv_writer.writeheader()

    for row in rows: # Iterate through data from query set result.
        if int(row[3]) in RESTRICTED_EMP_TYPE_LST: # Check for restiricted employee type
            data = {
                "SSN": row[1],
                "Name": row[2],
                "Type": row[3]
            }
            csv_writer.writerow(data) # Add row to csv file.

