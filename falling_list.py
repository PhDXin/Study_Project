num=[3,333,1]
falling = True
length=len(num)
for i in range(length):
    if i != 0:
        if num[i-1]<num[i]:
            falling = False
print(falling)
