class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def details(self):
      print(self.name,"is studying")

accountant =person("Joe ","34","Male")
print(accountant.name)
print(accountant.age)
accountant.details()
connsultant = person("Martha","56","Female")
print(connsultant.gender)
print(connsultant.age)

doctor = person("James","27","Male")
print(doctor.name)
doctor.details()




