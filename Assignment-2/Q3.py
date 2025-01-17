import random
import math
l=[]
for i in range(100):
    x=random.randint(100,900)
    l.append(x)
print(l)
countodd=0
counteven=0
countprime=0
for i in l:
    if i%2==0:
        counteven+=1
    else:
        countodd+=1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        countprime+=1
print(f'number of even, odd, prime numbers are {counteven}, {countodd}, {countprime}')
