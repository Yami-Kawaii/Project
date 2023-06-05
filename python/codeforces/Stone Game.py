t = int(input())
for _ in range(t):
    moves = 0
    n = int(input())
    a = list(map(int,input().split(" ")))
    min_,max_ = min(a),max(a)
    min_index,max_index = a.index(min_),a.index(max_)
    last_index = a.index(a[-1])
    while True:
        print(a)
        if a[0] == min_ or a[0] == max_:
            a.pop(0)
            moves += 1
        elif a[-1] == min_ or a[0] == max_:
            a.pop(-1)
            moves += 1
        if min_ not in a and max_ in a:
            if max_index > abs(last_index-max_index):
                a.pop(0)
                moves += 1
            else:
                a.pop(-1)
                moves += 1
        elif min_ in a and max_ not in a:
            if min_index > abs(last_index-min_index):
                a.pop(0)
                moves += 1
            else:
                a.pop(-1)
                moves += 1
        elif min_ not in a and max_ not in a:
            break
    print(moves)