import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")

conn.execute("INSERT INTO Employer(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
           VALUES(1,'Mageto','mark',21,5600.00,'employer')")
conn.execute("INSERT INTO Employer(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
           VALUES(2,'John','Ebar',21,5600.00,'Manager')")
conn.execute("INSERT INTO Employer(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
           VALUES(3,'Lewis','Opiyo',21,5600.00,'chef')")
conn.execute("INSERT INTO Employer(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
           VALUES(4,'Claire','Blair',21,5600.00,'HR')")

conn.commit()
print("Successfully Inserted values into Employer table")