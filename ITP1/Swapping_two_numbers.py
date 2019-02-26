while True:
    x,y = map(int,input().split())
    if x==0 and y==0:
        break
    big = max(x,y)
    small = min(x,y)
    print(small,big)