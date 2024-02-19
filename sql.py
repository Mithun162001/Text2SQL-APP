import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('test.db')

# Creating a cursor object using the cursor() method 
cursor = conn.cursor()

# Creating table as per requirement
table = """CREATE TABLE IF NOT EXISTS STUDENT(NAME VARCHAR(20), 
            SUBJECT VARCHAR(30), AGE INT, MARKS INT);"""
cursor.execute(table)

# Query to insert record
cursor.execute("""INSERT INTO STUDENT (NAME, SUBJECT, AGE, MARKS) 
               VALUES ('Rohan', 'Data Science', 12, 200);""")
cursor.execute("""INSERT INTO STUDENT (NAME, SUBJECT, AGE, MARKS)
                VALUES ('Allen', 'Database', 12, 200);""")
cursor.execute("""INSERT INTO STUDENT (NAME, SUBJECT, AGE, MARKS)
                VALUES ('Martha', 'Maths', 15, 100);""")
cursor.execute("""INSERT INTO STUDENT (NAME, SUBJECT, AGE, MARKS)
                VALUES ('Palak', 'CS50', 15, 200);""")
cursor.execute("""INSERT INTO STUDENT (NAME, SUBJECT, AGE, MARKS)
                VALUES ('Parak', 'C Programming', 15, 200);""")

# Displaying the data inserted
print("Data inserted in the table: ")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()