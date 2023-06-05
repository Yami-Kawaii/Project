n = int(input())
solve = 0
if n >= 1 and n <= 1000:
    for _ in range(n):
        judge = 0
        lst = list(map(int,input().split(" ")))
        for i in lst:
            if i == 1:
                judge += 1
        if judge >= 2:
            solve += 1
    print(solve)