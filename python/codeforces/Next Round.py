data = list(map(int,input().split(" ")))
scores = list(map(int,input().split(" ")))
moves = 0
k = data[1]
if len(scores) == data[0]:
    for i in scores:
        if i > k:
            moves += 1
        else:
            continue
print(moves)