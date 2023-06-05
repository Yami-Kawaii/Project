w = int(input())
ans = "NO"
moves = 0
if w >= 1 and w <= 100:
    if w % 2 == 0:
        for i in range(1,w+1):
            if i % 2 == 0:
                moves += 1
if moves >= 2:
    print("YES")
else:
    print("NO")