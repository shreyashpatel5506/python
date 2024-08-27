import random


list =[]
for i in range(10) :
    list.append(random.randint(0,100))
print(list)
number =int(input("enterr  the number"))
count=int(0)
for i in range(len(list)) :
    if number<list[i] :
        count+=1
if(count==len(list)):
    print("enter elemenet is smaller than all list member")
    
