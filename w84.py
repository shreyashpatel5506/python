str=input("enter a string::::")
charcter=input("entef a charcter which you want to count")
count=int(0)
for i in range(len(str)) :
    if charcter==str[i] :
        count+=1
        
print(count)