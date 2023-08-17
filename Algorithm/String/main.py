# number=int(input())
# if number>10:
#     print("YES")
# else:
#     print("NO")
# text=input()
# sum=0
# for i in range(len(text)):
#     sum+=int(text[i])
# print(sum)

# x=input()
# n=len(x)
# sum=0
# for i in range(n):
#     if n==1:
#         sum=int(n)
#     elif n==2:
#         sum=int(n[0])+int(n[1])
#     else:
#         sum=int(x[n-1])+int(x[n-2])+int(x[n-3])
# print(sum)

# text=input()
# result=0
# for i in range(len(text)):
#     if text[i]=='a'or text[i]=='A':
#         result+=1 
# if result>0:
#     print(result)

# n=int(input())
# result=""
# for i in range(n):
#     for j in range(n-i):
#         result+="X"
#     result+="\n"
# print(result)

text=input()
result=""
for i in range(len(text)):
    result+=text[len(text)-1-i]
print(result)

# text=input()
# result=""
# for i in range(len(text)):
#     result=text(len(text)-i-1)
# print(result)