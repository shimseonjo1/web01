import pyodbc 

def dbconn():
    server = '127.0.0.1' 
    database = 'DoItSQL' 
    username = 'sa' 
    password = 'qwer1234'

    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+ password)
    return conn