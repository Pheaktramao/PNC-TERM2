def sum(n1,n2):
    return n1+n2
def sumFromTo(array):
    if len(array)==2:
        total=0
        n1=int(array[0])
        if n1>int(array[1]):
            total=0
        else:
            while n1<=int(array[1]):
                total=sum(total,n1)
                n1+=1
        return total
    else:
        return "YOU GOT ERROR"
number=eval(input())
print(sumFromTo(number))