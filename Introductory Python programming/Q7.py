#7.1
f1=open("file.txt","w+")
text="cognitive computing"
f1.write(text)
f1.seek(0)
content=f1.read()
print(content)
f1.close()

#7.2
f2=open("file.txt","a+")
text=" UCS420 "
f2.write(text)
f2.seek(0)
print(f2.read())
f2.close()

#7.3
f3=open("file.txt","r")
l=f3.readlines()
count=len(l)
print("number of lines in text file are",count)



