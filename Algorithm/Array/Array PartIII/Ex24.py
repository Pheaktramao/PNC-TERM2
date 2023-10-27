# Ex1 - Array
# input1: ['banana','coconut','mango']
# input2: ['a','o']
# output:
# {'a': 4, 'o': 3]

def count_letter(word,value):
    count=0
    for i in range(len(word)):
        for j in range(len(word[i])):
            if word[i][j]==value:
                count+=1
    return count
Array=eval(input("Enter array:"))
n=eval(input("Enter arr:"))
newArr=[]
obj={}
for i in range(len(n)):
    obj[n[i]]=(count_letter(Array,n[i]))
newArr.append(obj)
print(newArr)