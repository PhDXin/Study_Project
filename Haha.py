s=input("Give me the string for hahafication:")
new_s=""
for i in s:
    if i =="h":
        new_s=new_s+"haha"+i
    else:
        new_s=new_s+i
print(new_s)
