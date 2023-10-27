# Ex9 - Array
# #Replace character by something
# input1: ['banana','coconut','mango']
# input2: ['a', '*']
# output:
def replace_word(word,array):
    result=""
    for i in range(len(word)):
        if word[i]==array[0]:
            result+=array[1]
        else:
            result+=word[i]
    return result
input1= ['banana','coconut','mango']
input2= ['c', '*']
newList=[]
for i in range(len(input1)):
    newList.append(replace_word(input1[i],input2))
print(newList)