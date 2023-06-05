t = int(input())
for _ in range(t):
    moves = 0
    counter = 0
    n = int(input())
    a = list(map(int,input().split(" ")))
    index_ = 0
    for i in range (n-1):
        min_,max_=min(a),max(a)
        if a[0] != min_:
            index_=a.index(min_)
            moves += 1
            a[0],a[index_] = min_,a[0]
        if a[-1] != max_:
            index_=a.index(max_)
            a[-1],a[index_] = max_,a[-1]
            moves += 1
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            moves += 1
        if a[i] < a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
            moves += 1
        if a[i] > a[-1]:
            a[i],a[-1] = a[-1],a[i]
            moves += 1
        if a[i] < a[0]:
            a[i],a[0] = a[0], a[i]
            moves += 1
        print(a)
    print(a)
    print(moves) 