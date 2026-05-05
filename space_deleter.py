s=input("Please input the string which you want to get rid of spaces:")
word_list=[]
word=""
s=s+" "
for i in s:
    if i != " " :
        word=word+i
    else:
        if word !="":
            word_list.append(word)
        word=""
print(word_list)
