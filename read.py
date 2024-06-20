import sqlite3


conn = sqlite3.connect('example.db')
print("Successfully Connected")

data = conn.execute("SELECT * FROM Employee")
for Employee in data:
    print("ID:", Employee[0])
    print("FIRSTNAME:", Employee[1])
    print("LASTNAME:", Employee[2])
    print("AGE:", Employee[3])
    print("SALARY:", Employee[4])
    print("POSITION:", Employee[5])

print("Successfully fetched data")
conn.close()
