# Ex7 - Array 2D
# arr2D = [
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','*','0'],
#   ['0','0','0','0']
# ]
#Where is index of "*"
# output: [2, 2]
def find_index_star(Array):
    index=[]
    for i in range(len(Array)):
        for j in range(len(Array[i])):
            if Array[i][j]=='*':
                index.append(i)
                index.append(j)
    return index
arr2D = [
  ['0','0','0','0'],
  ['0','0','0','0'],
  ['0','0','*','0'],
  ['0','0','0','0']
]
print(find_index_star(arr2D))