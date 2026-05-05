s=input("Give me the string you want to invert:")
word=s.split(" ")
word_inverted=[]
length=len(word)
for i in range(length-1,-1,-1):
    word_inverted.append(word[i])
print(word_inverted)
sentence =""
for i in word_inverted:
    sentence = sentence+i+" "
print(sentence)

