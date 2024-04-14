class Person:
    # private attribute and methods are meant to be used only within the class and 
    #...are not  accessible from outside the class

    __name = "anonymous"

    def __hellow(self):
        print( "hellow person!")

    def welcome(self):
        self.__hellow()


P1 = Person()
print(P1.welcome())
