text=input()
PointA=0
PointB=0
sum=0
for i in range(len(text)):
    if text[i]=='A' or text[i]=='a':
        PointA=10
    elif text[i]=='B' or text[i]=='b':
        PointB=20
sum=PointA+PointB
print(sum)