# Ex3 - basic 3
arr = [1, 0, 0, 1, 0]

#1 - Replace 0 with x
for i in range(len(arr)):
  if arr[i]==0:
    arr[i]="X"
print(arr)
#2 - Move 0 before 1
arr.sort()
print(arr)
#   Output: [0, 0, 0, 1, 1]