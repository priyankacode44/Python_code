"""class car:  #parent class/base class

# when one class(child/derived)derives the properties and methods  of another class(Parent/base)
# Types of 
#single inheritance(one parent and one child class)

    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(car):   #child class "ToyotaCar"

    def __init__(self,name):
        self.name=name

class fortunerCar(ToyotaCar):

    def __init__(self, type):
        self.type=type

c1 = fortunerCar("SUV")   #multilevel inheritance..
#print(c1.name)
#print(c1.start())
print(c1.type)
c1.start()"""



#multiple Inheritance

"""class A:
    varA = "welcome to the class A"

class B:
    varB = "Welcome to the class B"

class C(A ,B):
    varC = "Welcome to the class C"

c1 = C()

print(c1.varC)
print(c1.varA)
print(c1.varB)"""


# Super Method
# super method is used to access methods of the parent class

"""class Car:

    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):

    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

c1 = ToyotaCar("fortuner","Electrical")
print(c1.type)
print(c1.name)"""

#class Method
#class method is bound to the class and receives the class as an  implicit first argument
# Note static method cant access or modifiy class state  and generally for utility

"""class person:
    name = "any"

    #def changemethod(self , name):
     #   person.name = name
    @classmethod
    def changemethod(cls , name):
       cls.name = name

p1=person()
p1.changemethod("priya")
print(p1.name)
print(person.name)"""

# Property  (learn getter and satter as a homework)
# we use @property decorator  on any method in the class to use the method as aproperty
class student :

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage (self):
        return str((self.math + self.chem + self.phy)/3) + "%"
    
s1 = student(98,94,95)
print(s1.percentage)

s1.phy =89
print(s1.percentage)
        

        



        