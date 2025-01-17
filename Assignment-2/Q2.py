t=(45,89.5,76,45.4,89,92,58,45)
maximum=max(t)
print("highest score",maximum)
print("index of highest score",t.index(maximum))
minimum=min(t)
print("lowest score",minimum)
count=0
for i in t:
    if i==minimum:
        count+=1
print("count of lowest score",count)
l=t[::-1]
print("list of reversed tuple",l)
score=int(input("enter score "))
if score in t:
    print("score found at index",t.index(score))
else:
    print("score is not present")
    
