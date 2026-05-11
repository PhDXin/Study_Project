l=[2,1,2,3,5,10,7,11,13,15,7,2,4,20,1,32,64]
def purge(l):
	counter=1
	l_purged=[]
	l_purged.append(l[0])
	while l_purged != l:
		if l[counter]>l[counter-1]:
			l_purged.append(l[counter])
			counter+=1
		else:
			l.pop(counter)
		print("l:",l)
	return l_purged
l_purged=purge(l)
print(l_purged)
