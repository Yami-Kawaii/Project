
import math
t = int(input()) 
for _ in range(t):
    n = 0
    lst = list(map(int,input().split(" ")))
    l,r = lst[0],lst[1]
    if l <= r:
        if r - l < l:
            n = int(r % l)
        else:
            if r % 2 == 0:
                n = int(r/2-1)
            else:
                n = int(math.floor(r/2))
    print(n)