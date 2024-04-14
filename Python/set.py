#set is the collection of unorderd elements
#Each element in the set must be unique and immutable

collection = {1,2,3,"priyanka","Pankaj" ,"Manushree"}
student={1,2,1,4,2,"World","Hellow","World"}  # it remove duplicate element from set output(1,2,4,"world","Hellow")

#to create empty set
collection = set()


#sets are mutable but their values are immutable

collection.add(1)
collection.add(2)
collection.add(1)
collection.add("Priyanka")
collection.add((1,2,3))
print(collection)     #output (1, 2, "Priyanka", (1,2,3))

set1 = {1,2,3}
set2 ={2,3,4}
print(set1.union(set2))   #return(1,2,3,4) removes all duplicate value  
print(set1.intersection(set2)) #return (2,3) return only common values


#WAP to entered 3 subject from user and store it in dictionary
dict = {}
x = int(input("enter chem :"))
y = int(input("enter math :"))
z = int(input("enter phy :"))
dict.update({"chem" : x})
dict.update({"math" : y})
dict.update({"phy" : z})
print(dict)


#WAP to Enter 9 and 9.0



