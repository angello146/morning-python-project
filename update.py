import sqlite3

conn = sqlite3.connect('example.db')
print("Successfully Connected")

data = conn.execute(
    "UPDATE Employee set salary=500000.00 where id=4",)
conn.commit()

data = conn.execute("Select * from Employee where id=4,")
for Employee in data:
    print("ID:", Employee[0])
    print("FIRSTNAME:", Employee[1])
    print("LASTNAME:", Employee[2])
    print("AGE:", Employee[3])
    print("SALARY:", Employee[4])
    print("POSITION:", Employee[5])