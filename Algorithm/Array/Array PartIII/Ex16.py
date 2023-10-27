def find_position_of_star(array):
    index=None
    for i in range(len(array)):
        if array[i]=='*':
            index=i
    return index
arr = ['0', '0', '*', '0', '0', '0', '0']
#find index of *
startAction=True
while startAction:
    currentPosition=find_position_of_star(arr)
    comand=input("Enter comand:") 
    if comand.lower()=='l' and currentPosition>0:
        arr[currentPosition]='0'
        arr[currentPosition-1]='*'
        print(arr)
    elif comand.lower()=='r' and currentPosition<len(arr)-1:
        arr[currentPosition]='0'
        arr[currentPosition+1]='*'
        print(arr)
    elif currentPosition==0:
        print("Please go right")
    elif currentPosition==len(arr)-1:
        print("Please go left")
    else:
        if comand.lower()=='stop':
            startAction=False
            print("Action has been stopped..")
        else:
            print("Unknown " + comand + " comand")