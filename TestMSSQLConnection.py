import pyodbc 

server = 'tcp:10.13.31.43,1433' 
database = 'LPDEV_mdaca3' 
username = 'mdaca' 
password = '$Pin123456' 

# Establish the database connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Obtain a cursor
cursor = cnxn.cursor()

# Execute the query
cursor.execute("SELECT @@version;") 

# Loop over the result set
for row in cursor:
    print(row)