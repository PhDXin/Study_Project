s=input("PLease give me a list seperated by ',':")
objct=""
l=[]
counter=1
for i in s:
	if i !=",":
		objct=objct+i
	else :
		if objct !="":
			l.append(objct)
		objct=""
l.append(objct)
print(l)
for i in l:
	print(str(counter)+"."+i)
	counter+=1
