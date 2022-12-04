import ceODBC

DSN = 'Driver=ODBC Driver 17 for SQL Server;Server=tcp:localhost,1433;Database=ceODBC;UID=ceodbc;PWD=atc'

conn = ceODBC.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from TestStrings")
for row in cursor:
    print(row)
