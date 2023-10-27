# Ex1 - String array
Text = "How are you?"

#1 - Display word by word from text
# word=""
# for i in range(len(Text)):
#     if Text[i]==" ":
#         word+=Text[i]
#         print(word)
#         word=""
#     else:
#         word+=Text[i]
# print(word)
#   How
#   are
#   you?
#2 - Create new array from text seperate by space
# word=""
# arr=[]
# for i in range(len(Text)):
#     if Text[i]==" " or i==len(Text)-1:
#         if i==len(Text)-1:
#             word+=Text[i]
#         arr.append(word)
#         word=""
#     else:
#         word+=Text[i]
# print(arr)
# ["How","are","you?"]

word=""
arr=[]
for i in range(len(Text)):
    if Text[i]==" " or i==len(Text)-1:
        if i==len(Text)-1:
            word+=Text[i]
        arr.append(word)
        word=""
    else: 
        word+=Text[i]
print(arr)