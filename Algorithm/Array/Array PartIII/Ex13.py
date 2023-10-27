# Ex1: 
arr = ['0', '0', 'x', '0', '0', '0', '0']

# #1 - Find index of x
# #2 - Replace x by 0 and replace 0 by x
# #3 - Move x to next position
#   ['0', '0', '0', 'x', '0', '0', '0']
# #4 - Move x to prevouis position
#   ['0', 'x', '0', '0', '0', '0', '0']
def indexOfX(array):
    index=None 
    for i in range(len(array)):
        if array[i].lower()=='x':
            index=i
    return index
arr = ['0', '0', 'x', '0', '0', '0', '0']
currentindex=indexOfX(arr)
comand=input("Enter:")
if comand=='right' and currentindex < len(arr)-1:
    arr[currentindex]='0'
    arr[currentindex+1]='x'
else:
    arr[currentindex]='0'
    arr[currentindex-1]='x'
print(arr)
# -------------------+------------------------  
# Ex2 
# arr = ['0', '0', 'x', '0', '0', '0', '0']
# Enter: right
# To move x to right
# ['0', '0', '0', 'x', '0', '0', '0']

# Enter: left
# To move x to left
# ['0', 'x', '0', '0', '0', '0', '0']
def indexOfX(array):
    index=None 
    for i in range(len(array)):
        if array[i].lower()=='x':
            index=i
    return index
arr = ['0', '0', 'x', '0', '0', '0', '0']
startAction=True
while startAction :
    currentindex=indexOfX(arr)
    comand=input("Enter comand:")
    if comand.lower()=='right' and currentindex < len(arr)-1:
        arr[currentindex]='0'
        arr[currentindex+1]='x'
    elif comand.lower()=='left':
        arr[currentindex]='0'
        arr[currentindex-1]='x'
    print(arr)
# ------------------------------------------
# Ex3
# arr = [
#   ['0', 'x', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]
# #1 - Where is the position of x
# #2 - Move x to last index in first row
#  [
#   ['0', '0', '0', 'x'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]
# #3 Move x to below
#  [
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', 'x'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', '0', '0', '0']
# ]