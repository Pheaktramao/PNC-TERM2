# We have an array2D:
# array2D = [
    #     ['0','0','0'],
    #     ['0','0','0'],
#     #     ['0','0','0']
#     # ]

# # step1:create function (findPositionOfStar) find the row and column position of capitain
#   result = [1,1] ([row,col])
# def findPositionOfStar(array):
#     positionofstar=[]
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j]=='0':
#                 positionofstar.append(i)
#                 positionofstar.append(j)
#     return positionofstar
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]
# print(findPositionOfStar(array2D))
# step2:create function (moveStartToNextRight) to move the capitain to next right
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]
# def moveStartToNextRight(array):
#     index=None
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if array[i][j]=='0':
#                 index=i
#     return index
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]
# startAction=True
# while startAction:
#     for i in range(len(array2D)):
#         currentPosition=moveStartToNextRight(array2D[i])
#         command=input("Enter comand:")
#         if command.lower=='r' and currentPosition< len(array2D)-1:
#             array2D[i][currentPosition]=0
#             array2D[i][currentPosition+1]='0'
#         print(array2D)
# step3:create function (moveStarToNextLeft) to move the capitain to next left
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]

# step4:create function (moveStarToNextUp) to move the capitain to next up
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]

# step5:create function (moveStarToNextDown) to move the capitain to next down
# array2D = [
#         ['0','0','0'],
#         ['0','0','0'],
#         ['0','0','0']
#     ]

# step6:to check the condition (with user input R or L or U or D)
#   1.If user enter 'R' called the function (moveStartToNextRight) 
#   2.If user enter 'L' called the function (moveStarToNextLeft) 
#   3.If user enter 'U' called the function (moveStarToNextUp)
#   4.If user enter 'D' called the function (moveStarToNextDown) 
# def findPositionOfStar(array):
#     positionStar = []
#     for i in range(len(array)) :
#         for j in range(len(array[i])):
#             if array[i][j] == "0":
#                 positionStar.append(i)
#                 positionStar.append(j)
#     return positionStar
# array2D = [
#     ['0','0','0'],
#     ['0','0','0'],
#     ['0','0','0']
# ]
# def moveLeft(arr,row,column):
#     arr[row][column]='0'
#     arr[row][column-1]='0'
#     return arr
# def moveRight(arr, row,column):
#     arr[row][column]='0'
#     arr[row][column+1]='0'
#     return arr
# def moveUp(arr, row,column):
#     arr[row][column]='0'
#     arr[row-1][column]='0'
#     return arr
# def moveDown(arr, row,column):
#     arr[row][column]='0'
#     arr[row+1][column]='0'
#     return arr

# array2D = [
#     ['0','0','0'],
#     ['0','0','0'],
#     ['0','0','0']
# ]
# startAction = True
# while startAction:
#     currentIndex=findPositionOfStar(array2D)
#     command = input("Enter comand:")
#     row=currentIndex[0]
#     column=currentIndex[1]
#     if command.upper() == 'L':
#         print(moveLeft(array2D, row, column))
#     elif command.upper() == 'R':
#         print(moveRight(array2D, row, column))
#     elif command.upper() == 'D':
#         print(moveDown(array2D,row,column))
#     elif command.upper() == 'U':
#         print(moveUp(array2D,row,column))
#     else:
#         if command.lower() == "stop":
#             startAction = False
#             print("Action has been stopped...")
#         else:
#             print("Unknown " + command + " command")
# # step7:print(array2D)
def makeArray(col):
    array=[]
    for j in range(col):
            array.append('0')
    return array
def display_grid(grid):
    result=""
    for j in range(len(grid)):
        for k in range(len(grid[j])):
            result+=grid[j][k]+" "
        result+="\n"
    return result
row=int(input("Enter row:"))
col=int(input("Enter col:"))
Arr2D=[]
for i in range(row):
    Arr2D.append(makeArray(col))
print(display_grid(Arr2D))

Arr2D=[
    ['*','0','0'],
    ['*','0','0'],
    ['*','0','0']
]
column=len(Arr2D[0])
# isFound=False
# for i in range(len(Arr2D)):
#     row=i
#     j=0
#     while j<len(Arr2D[i]):
#         if Arr2D[0][j]!='*' and not isFound:
#             isFound=True
        
#         j+=1
# if isFound:
#     print("LOST")
# else:
#     print("WIN")

isRun=False
for i in range(len(Arr2D)):
    row=i
    j=0
    while j<len(Arr2D[i]):
        if Arr2D[i][0]!='*' and not isRun:
            isRun=True
        j+=1
if isRun:
    print("LOST")
else:
    print("WIN")