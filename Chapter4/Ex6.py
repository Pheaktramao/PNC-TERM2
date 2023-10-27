# Ex5 - Array 2D
# We have 2 input row and column create array 2D with value '0'
# Case:
# row: 2
# col: 2
# output:
# [['0','0'],['0','0']
# def createArray(col):
#     arr=[]
#     for i in range(col):
#         arr.append('0')
#     return arr
# row=int(input("Enter row: "))
# col=int(input("Enter column:"))
# Arr2D=[]
# for i in range(row):
#     Arr2D.append(createArray(col))
# print(Arr2D)

# def find_indexOfX(array):
#     index=None
#     isUnique=False
#     for i in range(len(array)):
#         if array[i]=='X' and not isUnique:
#             array[i+1]='X'
#             array[i]=0
#             isUnique=True
#     return array
# Arr=[0,0,0,'X',0,0]
# print(find_indexOfX(Arr))

# def find_index(array):
#     index=None
#     for i in range(len(array)):

# def findPositionOfStar(array):
#     positionStar = []
#     for i in range(len(array)) :
#         for j in range(len(array[i])):
#             if array[i][j] == "*":
#                 positionStar.append(i)
#                 positionStar.append(j)
#     return positionStar

# def moveLeft(arr):
#     return "Go Left"
# def moveRight(arr):
#     return "Go Right"
# def moveUp(arr):
#     return "Go Up"
# def moveDown(arr):
#     return "Go Down"

# array2D = [
#     ['0','0','0'],
#     ['0','*','0'],
#     ['0','0','0']
# ]
# startAction = True
# while startAction:
#     command = input()

#     if command.upper() == 'L':
#         print(moveLeft(array2D))
#     elif command.upper() == 'R':
#         print(moveRight(array2D))
#     elif command.upper() == 'D':
#         print(moveDown(array2D))
#     elif command.upper() == 'U':
#         print(moveUp(array2D))
#     else:
#         if command.lower() == "stop":
#             startAction = False
#             print("Action has been stopped...")
#         else:
#             print("Unknown " + command + " command")

def find_indexOfX(array):
    index=None
    for i in range(len(array)):
        if array[i]=='X':
            index=i
    return index
Array=eval(input())
isStop=False
while not isStop:
    currentPosition=find_indexOfX(Array)
    command=input("Enter Command: ")
    if command=='r' and currentPosition<len(Array)-1:
        Array[currentPosition]=0
        Array[currentPosition+1]='X'
    elif command=='l' and currentPosition>len(Array):
        Array[currentPosition+1]=0
        Array[currentPosition]='X'
    print(Array)