# Read 'Batch' table from Learning database via python using venv

import psycopg2

connection = psycopg2.connect(database="Learning", user="postgres", password="password", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from batch;")

# Fetch all rows from database
records = cursor.fetchall()
for record in records:
    print("Data from Database:- ", record)


# Write or insert into 'Batch' table from Learning database via python using venv

import psycopg2

connection = psycopg2.connect(database="Learning", user="postgres", password="password", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("insert into batch (batch_id, quantity) values ('B4',10);")



# Read 'Batch' table from Learning database via python using venv

import psycopg2

connection = psycopg2.connect(database="Learning", user="postgres", password="password", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from batch;")

# Fetch all rows from database
records = cursor.fetchall()
for record in records:
    print("Data from Database:- ", record)

# Commit the changes to database
connection.commit()


# Close the connection
connection.close()