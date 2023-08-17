# Ex1
# 1 - Get value from input as a string
# 2 - count how many letter that string contains
# 3 - display one letter by one letter
# 4 - check if all text is the same letter say "Okay" otherwise say "No"
# 5 - check if in string contains [ sign open and ] sign close
# # 6 - check how many letter in [ ]
# text=input()
# result=""
# isTrue=False
# for i in range(len(text)):
#     if text[0].upper()==text[i].upper() and not isTrue:
#         result="Okay"
#     else:
#         result="No"
#         isTrue=True
# print(result)
#
# Ex2
# 1 - Get value from input as a string
# 2 - display one letter by one letter using for loop
# 3 - check if in string contains single quote ' ' open and close
# 4 - get only letter inside single quote ' '
# 5 - get only letter outside single quote ' '
# text=input()
# isfound=False
# result=""
# for i in range(len(text)):
#     if text[i]!="'" and not isfound:
#         result+=text[i]
#     else:
#         if text[i]=="'":
#             isfound=not isfound
# print(result)
# Ex3
# 1 - Get value from input as a string
# 2 - display one letter by one letter using for loop
# 3 - check if in string contains ! say "Yes" otherwise say "No"
# text=input()
# result=""
# for i in range(len(text)):
#     if text[i]=="!":
#         result="Yes"
#     else:
#         result="No"
# print(result)
#1-Get value of number from input as a string
#2-display one by one each number in string
#3-sum number before number 6 and after number 6
# EX7
# text=input()
# sum=0
# result=""
# for i in range(len(text)):
#     if text[i]!="6":
#         sum+=int(text[i])
#     else:
#         result="6"
# if result=="6":
#     print(sum)
# else:
#     print("No number 6")
# Ex4
# 1 - Get value of number from input as string
# 2 - display one by one each character (number) in string
# 3 - check wich number is biggest and smallest number in string
# text=input()
# small=int(text[0])
# big=int(text[0])
# for i in range(len(text)):
#     if int(text[i])<small:
#         small=int(text[i])
#     elif int(text[i])>big:
#         big=int(text[i])
# print(small, big)



# text=input()
# result=""
# sum=""
# for i in range(len(text)):
#     if text[i]=="X":
#         sum+=text[i]
#     else:
#         result="X"
# if result=="X":
#     print(sum)
# else:
#     print("No X")

# text=input()
# result=""
# for i in range(len(text)):
#     if text[i]=="[":
#         result+=text[i]

# text1=input()
# text2=input()
# text3=input()
# result=""
# result1=""
# result2=""
# for i in range(len(text1)):
#     result+=text1[i]
# for i in range(len(text2)):
#     result1+=text2[i]
# for i in range(len(text3)):
#     result2+=text3[i]
# if result==result1:
#     print("Confirmed")
# elif result1==result2:
#     print("Confirmed")
# elif result2==result:
#     print("Confirmed")
# else:
#     print("Not Match")

text=input()
n1=""
n2=""
isStop=False
for i in range(len(text)):
    if text[i]!="|"and not isStop:
        n1+=text[i]
    else:
        if isStop:
            n2+=text[i]
        isStop=True
if int(n1) > int(n2):
    print("The biggest number is,"int(n1))
elif int(n1)<int(n2):
    print("The biggest number is," int(n2))
else:
    print("The number is equal")