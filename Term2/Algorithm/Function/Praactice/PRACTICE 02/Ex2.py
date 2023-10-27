# def getComment(grade):
#     if grade > 10:
#         return “Good”

# print(getComment(12) + getComment (8))

def getComment(grade):
    result=""
    if grade>10:
        result="Good"
    else:
        result="Bad"
    return result
n=int(input())
print(getComment(n))