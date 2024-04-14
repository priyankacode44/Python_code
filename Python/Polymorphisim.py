#Polymorphism: Operator Overloading
# when the  same operator is allowed to have different meaning according to the context
# Dunder ----__add__
class complex:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showtime(self):
        print(self.real,"i+", self.img,"j")

    def __add__(self , c2):
        newReal= self.real + c2.real
        newImg = self.img + c2.img
        return complex(newReal ,newImg)

c1 = complex(4,3)
c1.showtime()

c2 = complex(5,6)
c2.showtime()

c3 = c1 + c2
c3.showtime()


