data=open("grades.txt","r")
list_grade=data.readlines()
counter = 0
for i in list_grade:
    counter += float(i)
print(counter/len(list_grade))
