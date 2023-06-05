t = int(input())
for _ in range(t):
    d = -1
    lst =list(map(int,input().split(" ")))
    a,b,c = lst[0],lst[1],lst[2]
    z = 2 * abs(a-b)
    if a > z or b > z or c > z:
        print(d)
    else:
        d = z/2+c
        while d>z:
            d -= z
        print(int(d))