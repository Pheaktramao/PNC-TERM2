# Ex2 - String array

# arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]

#1 - How many banana in list
# count=0
# for i in range(len(arr)):
#     if arr[i]=='banana' or arr[i]=='Banana':
#         count+=1
# print(count)
#2 - How many letter "o" in list
# count=0
# for i in range(len(arr)):
#     word=arr[i]
#     for j in range(len(word)):
#         if word[j]=="o" or word[j]=="O":
#             count+=1
# print(count)
#3 - Replace banana by Jackfruit
# for i in range(len(arr)):
#     if arr[i]=='banana' or arr[i]=='Banana':
#         arr[i]="Jackfruit"
# print(arr)
#4 - Create new list with unique fruit
def checkValue(Value,list):
    isUnique=True
    for i in range(len(list)):
        if Value==list[i]:
            isUnique=False
    return isUnique
arr = ["banana","Banana","Apple","coconut", "mango", "coconut"]
list=[]
for i in range(len(arr)):
    if checkValue(arr[i],list):
        list.append(arr[i])
print(list)
# ["banana","Apple","coconut", "mango"]
#5 - Create new list store only letter "A" and "C" from list