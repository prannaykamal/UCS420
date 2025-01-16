import random

#9.1
for i in range(5):
    print(random.randint(1,100))

#9.2
n1=random.randint(1,100)
print(n1)
for i in range(2,n1):
    if n1%i==0:
        print("not a prime")
        break
else:
    print("prime")

#9.3
dice=random.randint(1,6)
print(dice)

#9.4
l=[1,2,3,4,5]
random.shuffle(l)
print(l)

#9.5
l1=[1,2,3,4,5]
x=random.choice(l)
print(x)

#9.6
length=int(input("enter length of password "))
password=""
for i in range(length):
    x=random.randint(33,126)
    chr1=chr(x)
    password=password+chr1
print(password)

#9.7
suit=["club","spade","heart","diamond"]
value=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
print(random.choice(value),"of",random.choice(suit))

