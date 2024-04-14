#Define circle class to create a circle  with radius r using constructor
"""class circle :

    def __init__(self, rad):
        self.rad = rad

# Define an area method of the class which calculates the area of the circle

    def area(self):
        return (3.14 * self.rad **2)
    

    def perimeter(self):
        return(2*3.14*self.rad)
    
c1 = circle(4)
print(c1.area())
print(c1.perimeter())"""

#________________________________________________________________

"""class Employee :

    def __init__(self, role, Department, Salary):
        self.role =role
        self.Department = Department
        self.Salary = Salary

    def showsDetails(self):
        print(self.role)
        print(self.Department)
        print(self.Salary)     


class Engineer(Employee):
      
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("SrEngineer","Product",2500000)
        


Eng = Engineer("Priyanka",34)
Eng.showsDetails()"""

class order :

    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self,od2):
        return self.price > od2.price


od1 = order("chips", 50)
od2 = order("tea", 30)

print(od1 > od2)
