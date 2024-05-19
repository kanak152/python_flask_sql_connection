# SQL Cheat Sheet for Flask MySQL Integration

## Author

**Kanak Sachan**

## Date

2024-05-19

## Description

This cheat sheet provides a quick reference to common SQL commands that can be used with your Flask application integrated with MySQL. It includes commands for creating tables, inserting data, querying data, updating records, and deleting data.

---

## Table of Contents

1. [Database Connection](#database-connection)
2. [Creating a Table](#creating-a-table)
3. [Inserting Data](#inserting-data)
4. [Querying Data](#querying-data)
5. [Updating Records](#updating-records)
6. [Deleting Records](#deleting-records)
7. [Advanced Queries](#advanced-queries)

---

## Database Connection

To connect to a MySQL database using Python:

```python
import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def close_db_connection(connection):
    if connection.is_connected():
        connection.close()

---
## creating-a-table
##Create a table named items:

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

##inserting-data
##Insert data into the items table:


INSERT INTO items (name, description) VALUES ('Item1', 'Description of Item1');
INSERT INTO items (name, description) VALUES ('Item2', 'Description of Item2');

#querying-data
##Python example:


connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", ("Item1", "Description of Item1"))
connection.commit()
close_db_connection(connection)


##Querying Data
##Select all records from the items table:

SELECT * FROM items;

SELECT * FROM items WHERE id = 1;


##Python example:

connection = get_db_connection()
cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT * FROM items")
items = cursor.fetchall()
close_db_connection(connection)


#updating-records

Update the description of an item:

UPDATE items SET description = 'Updated Description' WHERE id = 1;

##Python example:
connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("UPDATE items SET description = %s WHERE id = %s", ("Updated Description", 1))
connection.commit()
close_db_connection(connection)

##Deleting Records
##Delete a record from the items table:


DELETE FROM items WHERE id = 1;

##Python example:
connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("DELETE FROM items WHERE id = %s", (1,))
connection.commit()
close_db_connection(connection)


##Python example:

connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("DELETE FROM items WHERE id = %s", (1,))
connection.commit()
close_db_connection(connection)


##Advanced Queries
##Join Queries
##Select data from two related tables:


SELECT a.column1, b.column2
FROM table1 a
JOIN table2 b ON a.id = b.foreign_id;


##Aggregate Functions
##Count the number of items:

SELECT COUNT(*) FROM items;


##Get the average value of a column:

SELECT AVG(column_name) FROM table_name;


Group By
Group results by a specific column:


SELECT column_name, COUNT(*) FROM table_name
GROUP BY column_name;
```
