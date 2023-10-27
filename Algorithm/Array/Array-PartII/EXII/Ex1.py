# Ex1 - basic 1
arr = ["banana","apple"]

#1 - How many "a" or "A" in list
# count=0
# for i in range(len(arr)):
#     word=arr[i]
#     for j in range(len(word)):
#         if word[j]=="a" or word[j]=="A":
#             count+=1
# print(count)
#2 - Create new array store letter difference from A
array=[]
for i in range(len(arr)):
    word=arr[i]
    isFound=False
    for j in range(len(word)):
        if word[j]=="a" or word[j]=="A" and not isFound:
            isFound=True
        else:
            array.append(word[j])
print(array)
#   Output: ["b", "n", "n", "p", "p", "l", "e"]