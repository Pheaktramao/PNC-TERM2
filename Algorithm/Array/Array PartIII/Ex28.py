# Ex5 - Array
# #Reverse text by index
# input1: ['banana','coconut','mango']
# input2: [0, 2]
# output:
# ['ananab','coconut','ognam']
def reverse_text(array,value):
    word=array[value]
    res=""
    for i in range(len(word)):
        res+=word[-1-i]
    return res
input1=eval(input())
input2=eval(input())
for i in range(len(input2)):
    res=reverse_text(input1,input2[i])
    input1[input2[i]]=res
print(input1)