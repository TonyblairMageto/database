import sqlite3

conn = sqlite3.connect('employee.db')
print("connected successfully")


conn.execute("""CREATE TABLE Employer(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(10))""")

print("Successfully created Employer ")

conn.close()
