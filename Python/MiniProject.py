import random
import string

"""target = random.randint(1,100)

while True:
    Userint = input("Guess the Number or Quite(Q) :")
    if(Userint == "Q"):
        break
    Userinput = int(Userint)
    if(Userinput == target):
        print("Sucess : you have Guessed the correct number" )
        break
    elif(Userinput > target):
        print("Number was too big....Take a smaller guess...Guess again..!!")
    else :
        print("Number was too small...Guess a bigger Number...")


print("--------Game Over-----------")"""
        
#----------------Random Password Generator--------------

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
#print(random.choice("hellow"))
charValue = string.ascii_letters + string.digits + string.punctuation
#print(random.choice(charValue))

pass_len =12
"""password = ""
for i in range(pass_len):
    password += random.choice(charValue)

print("your password is :",password)"""

# List comprehension [function for i in range(n)]
res = "".join([random.choice(charValue)for i in range(pass_len)])
print(res)
