#Datatype

number =60  #Integer
num =45.36 #Float
greeting ="Hello there" #string
Ispythonintresting =True #boolean
fruits =["banana","Mango","apple"] #List
cars =("Bmw","Mercedes" "Toyota", "v8") #Tuple
Countries ={"Kenya","Tanzania","Uganada"} #Set
Student ={
    "firstname":"Gold",
    "Age":19,
    "Course":"MIT",
    "Nationality": "Kenyan",
    #this is  a dictionary
}
print(num)
print(Ispythonintresting)
print(fruits)
print(cars)
print(Countries)
print(Student["firstname"],)

#Determine data type
print(type(Ispythonintresting))
print(type(cars))

#Typecasting  is connverting one data type to another.
print(int(num))
print(float(number))