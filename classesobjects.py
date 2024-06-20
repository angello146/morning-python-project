#A class is a blueprint of an object.
#Object is an instance of a class
class person:
    #Properties/Attribute/Variable/Characteristic
    name = "Patrick"
    age = 18
    height = 2.1



    #Method/Function/Behaviour
    def walk(self):
        print("Personn is walking")


accountant = person() #Creating an object
accountant.walk()


teacher = person ()
teacher.walk()