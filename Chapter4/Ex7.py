# Ex6 - Array 2D
# arr2D = [
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','0','0'],
#   ['0','0','0','0']
# ]
# Display result in console:
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
def display_grid(Arry2D):
    result=""
    for i in range(len(Arry2D)):
        for j in range(len(Arry2D[i])):
            result+=Arry2D[i][j]+ " "
        result+="\n"
    return result
arr2D = [
  ['0','0','0','0'],
  ['0','0','0','0'],
  ['0','0','0','0'],
  ['0','0','0','0']
]
print(display_grid(arr2D))