def removeMinuses(string):
    result=""
    for i in range(len(string)):
        if string[i]!="-":
            result+=string[i]
    return result
isContinue=True
while isContinue:
    text=input("Enter a word:")
    print("word without minus:"+removeMinuses(text))
    letter=input("Do you want to continue(Y/N)?")
    if letter.upper()=="N":
        isContinue=False
