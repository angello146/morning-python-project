import sqlite3

conn = sqlite3.connect('example.db')
print("Successfully Connected")

conn.execute("INSERT INTO Employee VALUES (1, 'Mark','Mugo',45,120000.00,'Manager') ")
conn.execute("INSERT INTO Employee VALUES (2, 'Jane','Njoroge',28,20000.00,'Admin') ")
conn.execute("INSERT INTO Employee VALUES (3, 'Martha','Mujoja',78,89000.00,'HR') ")
conn.execute("INSERT INTO Employee VALUES (4, 'Ann','Kirui',55,100000.00,'Receptonist') ")
conn.execute("INSERT INTO Employee VALUES (5, 'George','Kamau',35,650000.00,'Marketer') ")
conn.execute("INSERT INTO Employee VALUES (6, 'Duke','Orodi',38,120000.00,'Consultant ') ")

conn.commit()
print("Successfully Inserted Values Into Employee Table")
