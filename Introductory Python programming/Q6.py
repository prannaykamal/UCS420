#6.1
str1=input("enter string ")
count=0
for i in str1:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels in string are",count)

#6.2
str2=input("enter string ")
rev2=str2[::-1]
print(rev2)

#6.3
str3=input("enter string ")
rev3=str3[::-1]
if str3==rev3:
    print("pallindrome")
else:
    print("not a pallindrome")
