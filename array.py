
courses = ["MIT","Cybersecurity","Datascience"]

print(courses)

#accessing an element in an array
print(courses[0])
print(courses[1])

#adding a new element in an array
courses.append("Android Development")
print(courses)

#deleting an element in an array
courses.remove("Cybersecurity")
print(courses)

#looping through an array
for course in courses:
    print(course)