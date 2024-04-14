str="this is a string,\n we are using it" #backslash n-to print in next line
print(str)

# concatenation
str1="pri";
str2="yanka"
print(str1+str2) #output---priyanka

#lengt calculate,this is also count spaces.
print(len(str1)) #output--3

#indexing, we can not modified the character
print(str1[1]) #output---(r)

#slicing
print(str[0:2])   #output---pr----staarting character involve but ending character are not involve
print(str[0:]) #output---pri
print(str[:1])  #output---p

#Negative index for slicing
fruit="apple"
print(fruit[-3:-1]) #output---pl----ending index not included

#
fruit.endswith("le")  #output---True

print(fruit.capitalize());  #output---Apple

name="My name is priyanka thakare"
print(name.replace("a","g"))
print(name.replace("priyanka","manushree"))
print(name.find("is"))
print(name.count("i"))

lstName=input("Enter your last Name")
print("length of last NAme :",len(lstName))  #output---

Example="Hi $ let me $ come to $"
print("count of dollar:",Example.count("$"))