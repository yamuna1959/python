import math
for i in range(1000,10000):
    num=int(math.sqrt(i))
    if(num*num==i):
        n=i
        while n!=0:
            r=n%10
            if r%2!=0:break
        else:print(i)
