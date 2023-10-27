# Ex6 - object
input1: ['banana','coconut','mango']
input2: [0,1]
# [
#   {0:'b',1:'a', 2:'n', 3: 'a', 4: 'n',5:'a'},
#   {0:'m',1:'a', 2:'n', 3: 'g', 4: 'o'},
# ]
def find_index(array,value):
    result=array[value]
    obj={}
    for i in range(len(result)):
        obj[i]=result[i]
    return obj
input1=eval(input("Enter input1:"))
input2=eval(input("Enter input2:"))
newArr=[]
for i in range(len(input2)):
    newArr.append(find_index(input1,input2[i]))
print(newArr)