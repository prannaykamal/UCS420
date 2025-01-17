A={34,56,78,90}
B={78,45,90,23}
U=A.union(B)
I=A.intersection(B)
SD=A.symmetric_difference(B)
subset=A.issubset(B)
superset=B.issuperset(A)
print(f'{U}\n{I}\n{SD}\n{subset}\n{superset}')
x=int(input("enter number "))
if x in A:
    A.remove(x)
else:
    print("not present")





        
