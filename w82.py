
def sumn(n,sum2) :
   
    sum2=sum2+n
    if(n==0) :
        return sum2
    return sumn(n-1,sum2)

RESULT=sumn(10,0)
print(RESULT)