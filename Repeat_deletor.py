ori_list=[1,1,2,8,8,4,1,1,1]
new_list=[]
l=len(ori_list)
new_list.append(ori_list[0])
for i in range(1,l):
	if ori_list[i-1]!= ori_list[i]:
		new_list.append(ori_list[i])
print(new_list)
		
