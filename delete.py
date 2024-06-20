import sqlite3

conn = sqlite3.connect('example.db')
print("Successfully Connected")

conn.execute("DELETE FROM Employee where id=6")
conn.commit()

data = conn.execute("SELECT * FROM Employee where id=6")

for Employee in data:
    print("ID:", Employee[0])
    print("FIRSTNAME:", Employee[1])
    print("LASTNAME:", Employee[2])
    print("AGE:", Employee[3])
    print("SALARY:", Employee[4])
    print("POSITION:", Employee[5])

