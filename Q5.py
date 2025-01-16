#5.1
l=[2,4,3,1,5]
maximum=max(l)
minimum=min(l)
print("maximum number in list is ",maximum)
print("minimum number in list is ",minimum)

#5.2
d={1:"one",2:"two",3:"three"}
key=int(input("enter key "))
print(d.get(key))

#5.3
l1=[2,4,3,1,5]
asc=sorted(l1)
desc=asc[::-1]
print(asc)
print(desc)

#5.4
d1={1:"one",2:"two",3:"three"}
d2={4:"four"}
d3={}
d3.update(d1)
d3.update(d2)
print(d3)
