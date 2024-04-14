"""count = 1    # iterator
while count <= 5 :   # for one round of loop called iteration
    print("I am Priyanka")
    count +=1

print(count)"""

#print number from 1 to 100

"""i = 1
while i <= 100 :
    print(i)
    i +=1 """

#print number from  100  to 1
    
"""i = 100
while i >= 1 :
    print(i)
    i -= 1"""


    # print the multiple numbers n time
 
"""i=1
n = int(input("Eneter the Number:"))
while i <= 10 :
 multi = n*i
 print(multi)
 i+=1
    """

#Print the element  of the following list
"""list =[1, 4, 9, 16, 25, 36, 49, 56, 81, 100]    #traverse=travel through each element
i=0
while i < len(list) :
  value=list[i]
  print(value)
  i += 1 """



"""tupl =(1, 4, 36, 16, 25, 36, 49, 56, 81, 100)
i=0
while i < len(tupl) :
    if(36==tupl[i]):
        print("found ", i)
        
        break
    else :
        print("finding")
    i += 1"""

"""i=1
while i <= 5:
    if(i == 4):
        i += 1
        continue 
    print(i)
    i += 1"""

#print the element using loop
    
"""list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i=0
while i < len(list):
    print(list[i])
    i +=1"""

    #Forloop
"""list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for value in list:
    if(value == 81):
        print("value found")
        break
    print(value)"""

    #range
"""seq= range(1,101,2)
for i in seq:
    print(i)"""

#range(print number from 1 to 100)
"""seq= range(1,100)
for i in seq:
    print(i)"""

#range(print number from 100 to 1)
"""seq= range(100,0,-1)
for i in seq:
    print(i)"""

#range(print number from 100 to 1)
"""seq= range(3,31,3)
for i in seq:
    print(i)"""

#use pass when we dont want to perform any work in range

"""for i in range(5):
    pass
print("some work is going")"""

# WAP to find sum of firest n number

"""i= 8
sum = 0
for i in range(0,i+1):
    sum +=i
print("total",sum)"""

# WAP to find factorial of first n number
i= 5
fact = 1
for i in range(1,i+1):
    fact *=i
print("total",fact)
    



