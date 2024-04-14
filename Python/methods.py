class student:
    #college_name ="ABC college"
#Methods
#It is a function that belongs to object

    """def __init__(self,name,marks):      #fullname = parameter
        self.name = name  #self.name= object ke andr nya create hone wala hai
        self.marks = marks

    def welcome(self):
        print("welcome",self.name , self.marks)

s1 = student("Pankaj", 97)
s1.welcome()
print(student.college_name)"""

#WAP to get average of 3 marks and print name

    """def __init__(self,name,marks1,marks2,marks3):
        self.name  =  name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        sum = (self.marks1 + self.marks2 + self.marks3)/3
        print("Average of marks: ",self.name, sum)

s1 = student("priyanka", 95, 94, 96)
s1.average()"""

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hellow():
        print("hellow")

    def get_average(self):
        sum = 0
        for value in self.marks:
            sum +=value
        print("hi,average value of",self.name,sum/3)



s1 = student("Manushree",[98, 97, 99])
s1.get_average()
s1.hellow()
"""s1.name = "Priyanka"
s1.get_average()"""

            
#Satatic Methods
#Static methods dont use self parameter(Work at class level)
# @staticmethod -----call as decorator


