# Ex4 - Array
# input: hello world
# output:
# ['hello', 'world']
# ['h','e','l','l','w','o','r','l','d']
# ['olleh','dlrow']
text=input("Enter: ")
word=""
Array=[]
for i in range(len(text)):
    if text[i]==" " or i==len(text)-1:
        word+=text[i]
        Array.append(word)
        word=""
    else:
        word+=text[i]
print(Array)
text=input("Enter: ")
word=""
Array=[]
for i in range(len(text)):
    if text[i]!=" ":
        word+=text[i]
    Array.append(word)
    word=""
print(Array)