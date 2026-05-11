l=[2,1,2,3,5]
def purge(l):
	length=len(l)
	l_purged=[]
	for i in range(1,length):
		if l[i]>l[i-1]:
			l_purged.append(l[i])
	return l_purged
l_purged=purge(l)
print(l_purged)
