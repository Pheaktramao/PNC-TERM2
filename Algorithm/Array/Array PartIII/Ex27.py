# Ex4 - Array
# #Get value by index
# input1: ['banana','coconut','mango']
# input2: [0, 2]
# output:
# {0: 'banana', 2: 'mango'}
def find_index(array,value):
    return array[value]
array=eval(input("Enter arr:"))
n=eval(input("Enter value:"))
Obj={}
for i in range(len(n)):
    Obj[n[i]]=(find_index(array,n[i]))
print(Obj)