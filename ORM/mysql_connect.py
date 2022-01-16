import mysql.connector
from mysql.connector import Error
from sqlalchemy.engine import create_engine

# Establishing a connection to mysql database
# UserName: root; HostName: localhost; DataBaseName: organization; Password: Pandu@mysql 
# The table 'Employee' already has some data to be used for querying
 
def create_server_connection(host_name, user_name, user_psswd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_psswd,
            database = db_name
        )
        print("Connection Established")
    except Error as err:
        print(f"An error of {err} occured")

    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"An error of {err} occured")

connection = create_server_connection("localhost", "root", "Pandu@mysql", "organization")

# Query 1: Using WHERE clause 
query1 = "SELECT*FROM employee WHERE basicsalary+da+hra<15000"
print(execute_query(connection, query1))

# Query 2: Using IN 
query2 = "SELECT*FROM employee WHERE basicsalary IN (2500,7000,4000)"
print(execute_query(connection, query2))

# Query 3: Using ORDER BY 
query3 = "SELECT id, name FROM employee ORDER BY da DESC LIMIT 5"
print(execute_query(connection, query3))
