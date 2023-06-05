#top bottom,n
#column, m
#Bot always looks bottom right

t = int(input())
for _ in range(t):
    trigger = False
    moves = 0
    lst = list(map(int,input().split(" ")))
    n,m,rb,cb,rd,cd = lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]
    while True:
        if rb == rd or cb == cd:
            break
        if rb < n and cb < m and not trigger:
            rb =+1
            cb =+1
            moves =+1
            trigger = True
        elif trigger:
            if rb == n and (cb-1<m)
    print(moves)
