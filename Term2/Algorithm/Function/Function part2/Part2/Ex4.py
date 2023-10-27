def removeCharacter(word,char):
    result=""
    for i in range(len(word)):
        if word[i]!=char:
            result+=word[i]
    return result

isContinue=True
while isContinue:
    word=input("Enter word: ")
    char=input("Enter the character to remove: ")
    print(removeCharacter(word,char))
    letter=input("Do you want to continue(Y/N)?")
    if letter.upper()=="N":
        isContinue=False