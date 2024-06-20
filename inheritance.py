#Parent class
class Animal:
  def speak(self):
      print('Animal is speaking')
#child class
class Bee (Animal):
    def buzz(self):
        print("Bee is Buzzing")
class Duck(Bee):
    def quacks(self):
     print("Duck is quacking")



a = Animal()
a.speak()

b = Bee()
b.buzz()

d =Duck
d.quacks()