# Ex1 - Array
# input1: hello
# output: olleh
text=input()
result=""
for i in range(len(text)):
    result+=text[-1-i]
print(result)
# -----
# Ex2 - Array
# input1: hello
output: ['o','l','l','e','h']
text=input()
Array=[]
for i in range(len(text)):
    Array.append(text[i])
print(Array)
# # -----
# # Ex3 - Array
# input1: ['banana','coconut']
# # ouput: ['ananab','tunococ']
def reverse_word(text):
    result=""
    for i in range(len(text)):
        result+=text[-1-i]
    return result
Array=eval(input("Enter Array:"))
newArr=[]
for i in range(len(Array)):
    newArr.append(reverse_word(Array[i]))
print(newArr)
# ----
# Ex4 - Array use only 1 function
def count_number(array,typeNumber):
    sum=0
    num=0
    if typeNumber=="odd":
        num=1
    elif typeNumber=="even":
        num=0
    for i in range(len(array)):
        if array[i]%2==num:
            sum+=array[i]
    return sum
Array=eval(input())
Command=input("Enter command:")
if Command=="odd":
    print(count_number(Array,Command))
elif Command=="even":
    print(count_number(Array,Command))
else:
    print("Command not found")
# print(count_number(Array))
# Case 1:
input: [1, 3, 4, 4]
# input: odd
# output: 4

# Case 2:
# input: [1, 3, 4, 4]
# input: even
# output: 8

# case 3:
# input: [1, 3, 4, 4]
# input: add
# output: Command not found
# -----
# Ex5 - Array
# input: ['banana', 'coconut']
# output: 
# [
#   {'b': 1},
#   {'a': 3},
#   {'n': 3},
#   {'c': 2},
#   {'o': 2},
#   {'u': 1},
#   {'t': 1},
# ]