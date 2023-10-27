def countCharacter(word,char):
    result=""
    for i in range(len(word)):
        if word[i]==char:
            for j in range(3):
                if word[i]==char:
                    result+=word[i]
    return result
nextstep="Y"
while nextstep=="Y":
    word=input("Enter the word: ")
    char=input("Enter the character to count: ")
    print(countCharacter(word,char))
    nextstep=input("Do you want to continue(Y/N): ").upper()