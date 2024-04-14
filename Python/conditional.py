marks=int(input("enter the marks"))

if(marks >= 90):
    Grade ="A"
elif(marks >=80 and marks < 90):
    Grade ="B"
elif(marks >=70 and marks < 80):
    Grade = "C"
else:
    Grade ="D"

print("Grade of the student",Grade);

##### Nesting condition

age = 34

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("you cannot drive")


# enter odd or even number
no = int(input("Enter a number"))

if(no %2 == 0):
    print("Number is Even number")
else:
    print("Number is odd")

    ##greatest of three number
    int1=int(input("Enter first number"))
    int2=int(input("Enter second number"))
    int3=int(input("Enter third number"))

    if(int1 >= int2 and int1 >= int3):
        print(int1)
    elif(int2 >= int3):
        print(int2)
    else:
        print(int3)



