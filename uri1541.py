import math
while True:
    a,b,c=map(int,input().split())
    if a==0 or b==0 or c==0:
        break
    area=a*b
    medida=math.ceil(area/(c/100))
    print(medida)
