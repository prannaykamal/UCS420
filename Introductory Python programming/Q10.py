import sys

#10.1
def add(a,b):
    return a+b
n1=int(sys.argv[1])
n2=int(sys.argv[2])
sum=add(n1,n2)
print(f"The sum of {n1} and {n2} is {sum}")

#10.2
str1=sys.argv[3]
print(len(str1))
