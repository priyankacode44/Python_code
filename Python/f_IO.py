  #read file
"""f = open("demo.txt","r")
#data =f.read()   #read file
#data =f.read(4)  #read first 4 character
readline1 = f.readline()  #read 1st line 
#print(data)
print(readline1)
readline2 = f.readline()
print(readline2)
f.close()"""

#write file

"""f1 = open("demo.txt","w")
f1.write("i am learning devops with python")
f1.close()"""

#append file

"""f1 = open("demo.txt","a")
f1.write("\nThen i move to devops \nThen i practice some projects")
f1.close()"""

#create file

"""f2 = open("sample.txt","w")  #we can create file by using "w" or "a"
#f2 = open("sample.txt","a")
f2.close()"""

#read and write
"""f2 = open("demo.txt","r+")  
f2.write("aaaaaaaaaaaaa")   #it overrides the starting letters
read2 = f2.read()  #it read next word where the pointer is after aaaaaa
print(read2)
f2.close()"""

#write and read
"""f2 = open("demo.txt","w+")  # Truncate all data 
print(f2.read()) 
f2.write("aaaaaaaaaaaaa")   
f2.close()"""

#(aapend)write and read
"""f2 = open("demo.txt","a+")  # append data from end 
f2.write("caaaaaaaaaaaa")   
print(f2.read())   #pointer eis in end so we cannt get no data in terminal
f2.close()"""

#syntax(it closes automatically)
"""with open("demo.txt","r") as f:
    data= f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("priyanka")"""


#install file then use pip install testflow
#use import for adding modue feature
"""import os

os.remove("sample.txt")"""


f = open("practice.txt","r")
#f.write("Hi everyone.\nwe are learning File I/O\nusing java.\nI like programming in java.")
data=f.read()
"""def name_change(data1):
    ser=data.replace("java","python")
    print(ser)"""

"""def name_change(data1):
    if(data.find("learning") != -1):
      print("available")
    else:
       print("Not available")

name_change(data)"""

"""def check_line():
   word = "programmingwith"
   data=True
   line = 1
   with open("practice.txt","r") as f:
    while data:
      data =f.readline()
      if(word in data):
        print(line)
        return
      line += 1

   return -1

print(check_line())"""

def check_even():
  count = 0
  f = open("count.txt","r")
  data = f.read()
  nums = data.split(",") 
  for value in nums:
    if(int(value) % 2 == 0):
     print(value)
     count +=1
      
check_even()



