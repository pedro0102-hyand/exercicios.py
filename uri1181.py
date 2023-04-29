l=int(input())
t=int(input())
m=[]
for i in range(12):
    line=[]
    for j in range(12):
        line.append(float(input()))
    m.append(line)
sum=0
x=0
for i in range(12):
    for j in range(12):
        if j>l :
            sum+=m[i][j]
            x=x+1
if t=='S':
    print('{:.1f}'.format(sum))
else:
    media=sum/x
