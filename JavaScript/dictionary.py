# Dictionary are used to stored values in the form of key value pairs
# They are unorderd,mutable(changeble),dont allow duplicate keys
# dont take key as list or dictionary beacuse it is changing

info = { "father"   :  "Pankaj",
         "Mother"   : "Priyanka",
         "Daughter" :  "Manushree",
         "relation" : ("Fa", "Ma", "Da"),
          "Age"     : [38, 34, 6]

}
print(info["father"])  #Output Pankaj

info["Mother"] = "Priya" #Output change Mother Name

print(info)

info["Surname"] = "Thakare" # add one more key value in info dict

print(info)

#creating null dictionary

null_dict = {}
null_dict["subj"] = "Python"
null_dict["Devops"] = True
print(null_dict)

#Nested dictionary

student ={
    "name" : "Priyanka",
    "subject" :{
        "phy" : 98,
        "chem" : 93,
        "math" : 90
    }

}
print (student)
print (student["subject"])
print(student["subject"]["chem"])
print(student.keys())   #return all outer keys
print(list(student.keys())) #typecast into list
print(len(student))   #length of the student(count of key)
print(student.values()) #return values
print(list(student.values())) # return all values in list form
print(student.items())   #returen key and value in tthe form of tupple
print(list(student.items()))   # still it returen key and value in tthe form of tupple
print(student.get("name"))    #returm  the value but if key value not present then it simply get None
print(student["Name2"])  #return the error because the key is not presesnt
student.update({"city" : "pune"})  #add the new  dict
print(student)