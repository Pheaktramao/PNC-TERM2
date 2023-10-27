def removeCharacter(word,char):
    result=""
    for i in range(len(word)):
        if word[i]!=char:
            result+=word[i]
    return result
word=input("Enter word: ")
char=input("Enter the character to remove: ")
print(removeCharacter(word,char))