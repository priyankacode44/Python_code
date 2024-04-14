#List, it is mutable(value can change)
list=[2,3,4,5]

# Tuple it is immutable(value not change)
list=(2,3,4,5)
list=(1,)
print(type(list))
print(list[1:3])  #sliceing
print(list.index(1))    #output--3

#WAP to input 3 movies from users and store in list

movlist=[]

mov1=input("Enter your 1 favorite movie :")
mov2=input("Enter your 2 favorite movie :")
mov3=input("Enter your 3 favorite movie :")

movlist.append(mov1)
movlist.append(mov2)
movlist.append(mov3)

print(movlist)


#WAP to check whwther list contains palidrome number

list=[1,2,3,2,1]

copy_list=list.copy()
copy_list.reverse()

if(copy_list==list):
    print("palidrome")
else:
    print("not palidrome")


#WAP to count gradeA from tuplelist
    
Grade=("C","D","A","A","B","B","A")
print(Grade.count("A"))


#Store above values in list and sort them in ascending order

Grade=["C","D","A","A","B","B","A"]
print(Grade.sort())
