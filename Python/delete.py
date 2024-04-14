#Delete
#used to delete object properties or object itself

class student:

    """def __init__(self,name):
        self.name = name

s1 = student("Priya")
print("name of the objecct :",s1.name)
del s1
print(s1.name)"""


#Private(attribute and Methods)
#conceptual implementation in python
# private attributes and methods are meant to be used only within the class and are not accessible from outside the class

    """def __init__(self, accnt, passw):
        self.accnt = accnt
        self.__passw = passw     #for private use (__)

    def reset(self):
        print(self.__passw)

s1 = student("1234","abcde")
print(s1.accnt)
print(s1.reset())
print(s1.__passw)"""



