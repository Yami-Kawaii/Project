t = int(input())
for _ in range(t):
    l,r,S = 0,0,[]
    n = int(input())
    s = input()
    if len(s) == 1:
        l,r = -1,-1
    elif len(s) == n:
        for i in s:
            if i == "a":
                l += 1
            elif i == "b":
                r += 1
            else:
                continue